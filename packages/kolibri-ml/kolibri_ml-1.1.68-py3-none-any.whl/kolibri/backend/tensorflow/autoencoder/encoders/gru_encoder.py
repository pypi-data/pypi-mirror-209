# encoding: utf-8

import numpy as np
import tensorflow as tf

from kolibri.backend.tensorflow.embeddings.base_embedding import BaseEmbedding
from kolibri.backend.tensorflow.layers import L


class GRUEncoder(tf.keras.Model):
    def __init__(self, embedding: BaseEmbedding, hidden_size: int = 1024):
        super(GRUEncoder, self).__init__()
        self.embedding = embedding
        self.hidden_size = hidden_size
        self.gru = tf.keras.layers.GRU(hidden_size,
                                       return_sequences=True,
                                       return_state=True,
                                       recurrent_initializer='glorot_uniform')

    def call(self, x: np.ndarray, hidden: np.ndarray) -> np.ndarray:
        if self.embedding.segment:
            x = (x, tf.zeros(x.shape))
        x = self.embedding.embed_model(x)
        output, state = self.gru(x, initial_state=hidden)
        return output, state

    def model(self) -> tf.keras.Model:
        x1 = L.Input(shape=(None,))
        x2 = L.Input(shape=(self.hidden_size,))
        return tf.keras.Model(inputs=[x1, x2],
                              outputs=self.call(x1, x2),
                              name='GRUEncoder')


if __name__ == "__main__":
    pass
