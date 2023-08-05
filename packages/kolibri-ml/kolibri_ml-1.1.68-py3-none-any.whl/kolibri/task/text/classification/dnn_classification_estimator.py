from kolibri import default_configs as settings
from kolibri.config import TaskType
from kolibri.config import override_defaults
from kolibri.task.dnn_estimator import DnnEstimator

try:
    from kolibri.backend.tensorflow.tasks.text.classification.models import get_model
    from kolibri.backend.tensorflow.embeddings import DefaultEmbedding, WordEmbedding
except Exception as e:
    pass

from kolibri.logger import get_logger
from kolibri.indexers.label_indexer import LabelIndexer

logger = get_logger(__name__)

KOLIBRI_MODEL_FILE_NAME = "classifier_kolibri.pkl"
DNN_MODEL_FILE_NAME = "classifier_dnn"


class DnnTextClassEstimator(DnnEstimator):
    """classifier using the sklearn framework"""

    name = 'dnn_classifier'

    provides = ["classification", "target_ranking"]

    requires = ["text_features"]

    component_type = "estimator"

    defaults = {

        "fixed":{
            "model": "bilstm",
            "embeddings": "default",
            "multi-label": False,
            "sequence_length": 'auto',
            "epochs": 1,
            "loss": 'categorical_crossentropy',
            "class-weight": False,
            "architecture":None

        },
        "tunable":{

        }
        # the models used in the classifier if several models are given they will be combined

    }

    def __init__(self, component_config=None):

        """Construct a new class classifier using the sklearn framework."""

        self.defaults = override_defaults(
            super().defaults, self.defaults)

        super().__init__(component_config)
        self.indexer = LabelIndexer(multi_label=self.get_parameter("multi-label"))
        if self.get_parameter('embeddings') == 'default':
            self.embeddings = DefaultEmbedding(task=TaskType.CLASSIFICATION,
                                               sequence_length=self.get_parameter("sequence_length"),
                                               indexer=self.indexer)
        elif self.get_parameter('embeddings') == 'word':
            self.embeddings = WordEmbedding(w2v_path=self.get_parameter("embedding_path"),
                                            task=TaskType.CLASSIFICATION,
                                            sequence_length=self.get_parameter("sequence_length"),
                                            indexer=self.indexer)
        elif self.get_parameter('embeddings') == None:
            self.embeddings = None

        self.clf = get_model(self.get_parameter('model'), embedding=self.embeddings, hyper_parameters=self.get_parameter("architecture"))
        self.classifier_type = type(self.clf)

    @classmethod
    def required_packages(cls):
        return ["tensorflow"]

    def process(self, document, **kwargs):
        """Return the most likely class and its probability for a document."""
        raw_results = None
        if not self.clf:
            # component is either not trained or didn't
            # receive enough training texts
            target = None
            target_ranking = []
        else:
            X = document.tokens
            classes, probabilities = self.clf.predict([X], top_k=settings.modeling['TARGET_RANKING_LENGTH'])


            # `predict` returns a matrix as it is supposed
            # to work for multiple examples as well, hence we need to flatten
            classes, probabilities = classes.flatten(), probabilities.flatten()

            if len(classes) > 0 and probabilities.size > 0:
                ranking = list(zip(list(classes),
                                   list(probabilities)))[:settings.modeling['TARGET_RANKING_LENGTH']]

                target = {"name": classes[0], "confidence": probabilities[0]}

                target_ranking = [{"name": class_name, "confidence": score}
                                  for class_name, score in ranking]
            else:
                target = {"name": None, "confidence": 0.0}
                target_ranking = []
        #            self.clf.classes_ = self.indexer.la

        document.label = target
        document.raw_prediction_results = raw_results
        document.set_output_property("raw_prediction_results")
        document.set_output_property("label")
        document.target_ranking = target_ranking
        document.set_output_property("target_ranking")