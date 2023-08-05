import itertools
from operator import mul
from functools import reduce

import numpy as np

from kolibri.backend.bn.DiscreteFactor import DiscreteFactor
from kolibri.backend.bn.Independencies import Independencies


class JointProbabilityDistribution(DiscreteFactor):
    """
    Base class for Joint Probability Distribution
    """

    def __init__(self, variables, cardinality, values):
        """
        Initialize a Joint Probability Distribution class.

        Defined above, we have the following mapping from variable
        assignments to the index of the row vector in the value field:

        +-----+-----+-----+-------------------------+
        |  x1 |  x2 |  x3 |    P(x1, x2, x2)        |
        +-----+-----+-----+-------------------------+
        | x1_0| x2_0| x3_0|    P(x1_0, x2_0, x3_0)  |
        +-----+-----+-----+-------------------------+
        | x1_1| x2_0| x3_0|    P(x1_1, x2_0, x3_0)  |
        +-----+-----+-----+-------------------------+
        | x1_0| x2_1| x3_0|    P(x1_0, x2_1, x3_0)  |
        +-----+-----+-----+-------------------------+
        | x1_1| x2_1| x3_0|    P(x1_1, x2_1, x3_0)  |
        +-----+-----+-----+-------------------------+
        | x1_0| x2_0| x3_1|    P(x1_0, x2_0, x3_1)  |
        +-----+-----+-----+-------------------------+
        | x1_1| x2_0| x3_1|    P(x1_1, x2_0, x3_1)  |
        +-----+-----+-----+-------------------------+
        | x1_0| x2_1| x3_1|    P(x1_0, x2_1, x3_1)  |
        +-----+-----+-----+-------------------------+
        | x1_1| x2_1| x3_1|    P(x1_1, x2_1, x3_1)  |
        +-----+-----+-----+-------------------------+

        Parameters
        ----------
        variables: list
            List of scope of Joint Probability Distribution.
        cardinality: list, array_like
            List of cardinality of each variable
        value: list, array_like
            List or array of values of factor.
            A Joint Probability Distribution's values are stored in a row
            vector in the value using an ordering such that the left-most
            variables as defined in the variable field cycle through their
            values the fastest.

        Examples
        --------

        """
        if np.isclose(np.sum(values), 1):
            super(JointProbabilityDistribution, self).__init__(
                variables, cardinality, values
            )
        else:
            raise ValueError("The probability values doesn't sum to 1.")

    def __repr__(self):
        var_card = ", ".join(
            [f"{var}:{card}" for var, card in zip(self.variables, self.cardinality)]
        )
        return f"<Joint Distribution representing P({var_card}) at {hex(id(self))}>"

    def __str__(self):
        return self._str(phi_or_p="P")

    def marginal_distribution(self, variables, inplace=True):
        """
        Returns the marginal distribution over variables.

        Parameters
        ----------
        variables: string, list, tuple, set, dict
                Variable or list of variables over which marginal distribution needs
                to be calculated
        inplace: Boolean (default True)
                If False return a new instance of JointProbabilityDistribution

        Examples
        --------
        """
        return self.marginalize(
            list(
                set(list(self.variables))
                - set(
                    variables
                    if isinstance(variables, (list, set, dict, tuple))
                    else [variables]
                )
            ),
            inplace=inplace,
        )

    def check_independence(
        self, event1, event2, event3=None, condition_random_variable=False
    ):
        """
        Check if the Joint Probability Distribution satisfies the given independence condition.

        Parameters
        ----------
        event1: list
            random variable whose independence is to be checked.
        event2: list
            random variable from which event1 is independent.
        values: 2D array or list like or 1D array or list like
            A 2D list of tuples of the form (variable_name, variable_state).
            A 1D list or array-like to condition over randome variables (condition_random_variable must be True)
            The values on which to condition the Joint Probability Distribution.
        condition_random_variable: Boolean (Default false)
            If true and event3 is not None than will check independence condition over random variable.

        For random variables say X, Y, Z to check if X is independent of Y given Z.
        event1 should be either X or Y.
        event2 should be either Y or X.
        event3 should Z.

        Examples
        --------

        """
        JPD = self.copy()
        if isinstance(event1, str):
            raise TypeError("Event 1 should be a list or array-like structure")

        if isinstance(event2, str):
            raise TypeError("Event 2 should be a list or array-like structure")

        if event3:
            if isinstance(event3, str):
                raise TypeError("Event 3 cannot of type string")

            elif condition_random_variable:
                if not all(isinstance(var, str) for var in event3):
                    raise TypeError("event3 should be a 1d list of strings")
                event3 = list(event3)
                # Using the definition of conditional independence
                # If P(X,Y|Z) = P(X|Z)*P(Y|Z)
                # This can be expanded to P(X,Y,Z)*P(Z) == P(X,Z)*P(Y,Z)
                phi_z = JPD.marginal_distribution(event3, inplace=False).to_factor()
                for variable_pair in itertools.product(event1, event2):
                    phi_xyz = JPD.marginal_distribution(
                        event3 + list(variable_pair), inplace=False
                    ).to_factor()
                    phi_xz = JPD.marginal_distribution(
                        event3 + [variable_pair[0]], inplace=False
                    ).to_factor()
                    phi_yz = JPD.marginal_distribution(
                        event3 + [variable_pair[1]], inplace=False
                    ).to_factor()
                    if phi_xyz * phi_z != phi_xz * phi_yz:
                        return False
                return True
            else:
                JPD.conditional_distribution(event3)

        for variable_pair in itertools.product(event1, event2):
            if JPD.marginal_distribution(
                variable_pair, inplace=False
            ) != JPD.marginal_distribution(
                variable_pair[0], inplace=False
            ) * JPD.marginal_distribution(
                variable_pair[1], inplace=False
            ):
                return False
        return True

    def get_independencies(self, condition=None):
        """
        Returns the independent variables in the joint probability distribution.
        Returns marginally independent variables if condition=None.
        Returns conditionally independent variables if condition!=None

        Parameters
        ----------
        condition: array_like
                Random Variable on which to condition the Joint Probability Distribution.

        Examples
        --------
        """
        JPD = self.copy()
        if condition:
            JPD.conditional_distribution(condition)
        independencies = Independencies()
        for variable_pair in itertools.combinations(list(JPD.variables), 2):
            if JPD.marginal_distribution(
                variable_pair, inplace=False
            ) == JPD.marginal_distribution(
                variable_pair[0], inplace=False
            ) * JPD.marginal_distribution(
                variable_pair[1], inplace=False
            ):
                independencies.add_assertions(variable_pair)
        return independencies

    def conditional_distribution(self, values, inplace=True):
        """
        Returns Conditional Probability Distribution after setting values to 1.

        Parameters
        ----------
        values: list or array_like
            A list of tuples of the form (variable_name, variable_state).
            The values on which to condition the Joint Probability Distribution.
        inplace: Boolean (default True)
            If False returns a new instance of JointProbabilityDistribution

        Examples
        --------
        """
        JPD = self if inplace else self.copy()
        JPD.reduce(values)
        JPD.normalize()
        if not inplace:
            return JPD

    def copy(self):
        """
        Returns A copy of JointProbabilityDistribution object

        Examples
        ---------
        """
        return JointProbabilityDistribution(self.scope(), self.cardinality, self.values)

    def minimal_imap(self, order):
        """
        Returns a Bayesian Model which is minimal IMap of the Joint Probability Distribution
        considering the order of the variables.

        Parameters
        ----------
        order: array-like
            The order of the random variables.

        Examples
        --------

        """
        from kolibri.backend.bn.BayesianNetwork import BayesianNetwork

        def get_subsets(u):
            for r in range(len(u) + 1):
                for i in itertools.combinations(u, r):
                    yield i

        G = BayesianNetwork()
        for variable_index in range(len(order)):
            u = order[:variable_index]
            for subset in get_subsets(u):
                if len(subset) < len(u) and self.check_independence(
                    [order[variable_index]], set(u) - set(subset), subset, True
                ):
                    G.add_edges_from(
                        [(variable, order[variable_index]) for variable in subset]
                    )
        return G

    def is_imap(self, model):
        """
        Checks whether the given BayesianNetwork is Imap of JointProbabilityDistribution

        Parameters
        ----------
        model : An instance of BayesianNetwork Class, for which you want to
            check the Imap

        Returns
        -------
        Is IMAP: bool
            True if given bayesian model is Imap for Joint Probability Distribution False otherwise

        Examples
        --------

        """
        from kolibri.backend.bn.BayesianNetwork import BayesianNetwork

        if not isinstance(model, BayesianNetwork):
            raise TypeError("model must be an instance of BayesianNetwork")
        factors = [cpd.to_factor() for cpd in model.get_cpds()]
        factor_prod = reduce(mul, factors)
        JPD_fact = DiscreteFactor(self.variables, self.cardinality, self.values)
        if JPD_fact == factor_prod:
            return True
        else:
            return False

    def to_factor(self):
        """
        Returns JointProbabilityDistribution as a DiscreteFactor object

        Examples
        --------
        """
        return DiscreteFactor(self.variables, self.cardinality, self.values)

    def pmap(self):
        pass
