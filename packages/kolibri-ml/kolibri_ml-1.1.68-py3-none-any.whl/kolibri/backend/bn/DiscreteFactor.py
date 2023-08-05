import logging
import warnings
from collections import namedtuple
from itertools import product

import numpy as np
import pandas as pd

from kolibri.backend.bn.tabulate import tabulate
from kolibri.backend.bn.factors_base import BaseFactor
from kolibri.backend.bn.state_name import StateNameMixin

State = namedtuple("State", ["var", "state"])


class DiscreteFactor(BaseFactor, StateNameMixin):
    """
    Base class for DiscreteFactor.
    """

    def __init__(self, variables, cardinality, values, state_names={}, *args, **kwargs):
        """
        Initialize a `DiscreteFactor` class.

        Defined above, we have the following mapping from variable
        assignments to the index of the row vector in the value field:
        +-----+-----+-----+-------------------+
        |  x1 |  x2 |  x3 |    phi(x1, x2, x3)|
        +-----+-----+-----+-------------------+
        | x1_0| x2_0| x3_0|     phi.value(0)  |
        +-----+-----+-----+-------------------+
        | x1_0| x2_0| x3_1|     phi.value(1)  |
        +-----+-----+-----+-------------------+
        | x1_0| x2_1| x3_0|     phi.value(2)  |
        +-----+-----+-----+-------------------+
        | x1_0| x2_1| x3_1|     phi.value(3)  |
        +-----+-----+-----+-------------------+
        | x1_1| x2_0| x3_0|     phi.value(4)  |
        +-----+-----+-----+-------------------+
        | x1_1| x2_0| x3_1|     phi.value(5)  |
        +-----+-----+-----+-------------------+
        | x1_1| x2_1| x3_0|     phi.value(6)  |
        +-----+-----+-----+-------------------+
        | x1_1| x2_1| x3_1|     phi.value(7)  |
        +-----+-----+-----+-------------------+

        Parameters
        ----------
        variables: list, array-like
            List of variables on which the factor is to be defined i.e. scope of the factor.

        cardinality: list, array_like
            List of cardinalities/no.of states of each variable. `cardinality`
            array must have a value corresponding to each variable in
            `variables`.

        values: list, array_like
            List of values of factor.
            A DiscreteFactor's values are stored in a row vector in the value
            using an ordering such that the left-most variables as defined in
            `variables` cycle through their values the fastest. Please refer
            to examples for usage examples.

        Examples
        --------

        """
        super().__init__(*args, **kwargs)
        if isinstance(variables, str):
            raise TypeError("Variables: Expected type list or array like, got string")

        values = np.array(values, dtype=float)

        if len(cardinality) != len(variables):
            raise ValueError(
                "Number of elements in cardinality must be equal to number of variables"
            )

        if values.size != np.product(cardinality):
            raise ValueError(f"Values array must be of size: {np.product(cardinality)}")

        if len(set(variables)) != len(variables):
            raise ValueError("Variable names cannot be same")

        if not isinstance(state_names, dict):
            raise ValueError(
                f"state_names must be of type dict. Got {type(state_names)}."
            )

        self.variables = list(variables)
        self.cardinality = np.array(cardinality, dtype=int)
        self.values = values.reshape(self.cardinality)

        # Set the state names
        super(DiscreteFactor, self).store_state_names(
            variables, cardinality, state_names
        )

    def scope(self):
        """
        Returns the scope of the factor i.e. the variables on which the factor is defined.

        Returns
        -------
        Scope of the factor: list
            List of variables on which the factor is defined.

        Examples
        --------
        """
        return self.variables

    def get_cardinality(self, variables):
        """
        Returns the cardinality/no.of states of each variable in `variables`.

        Parameters
        ----------
        variables: list, array-like
                A list of variable names.

        Returns
        -------
        Cardinality of variables: dict
            Dictionary of the form {variable: variable_cardinality}

        Examples
        --------
        """
        if isinstance(variables, str):
            raise TypeError("variables: Expected type list or array-like, got type str")

        if not all([var in self.variables for var in variables]):
            raise ValueError("Variable not in scope")

        return {var: self.cardinality[self.variables.index(var)] for var in variables}

    def get_value(self, **kwargs):
        """
        Returns the value of the given variable states. Assumes that the arguments
        specified are state names, and falls back to considering it as state no if
        can't find the state name.

        Parameters
        ----------
        kwargs: named arguments of the form variable=state_name
            Spcifies the state of each of the variable for which to get
            the value.

        Returns
        -------
        value of kwargs: float
            The value of specified states.

        Examples
        --------

        """
        for variable in kwargs.keys():
            if variable not in self.variables:
                raise ValueError(f"Factor doesn't have the variable: {variable}")

        index = []
        for var in self.variables:
            if var not in kwargs.keys():
                raise ValueError(f"Variable: {var} not found in arguments")
            else:
                try:
                    index.append(self.name_to_no[var][kwargs[var]])
                except KeyError:
                    logging.info(f"Using {var} state as number instead of name.")
                    index.append(kwargs[var])
        return self.values[tuple(index)]

    def set_value(self, value, **kwargs):
        """
        Sets the probability value of the given variable states.

        Parameters
        ----------
        value: float
            The value for the specified state.

        kwargs: named arguments of the form variable=state_name
            Spcifies the state of each of the variable for which to get
            the probability value.

        Returns
        -------
        None

        Examples
        --------
        """
        if not isinstance(value, (float, int)):
            raise ValueError(f"value must be float. Got: {type(value)}.")

        for variable in kwargs.keys():
            if variable not in self.variables:
                raise ValueError(f"Factor doesn't have the variable: {variable}")

        index = []
        for var in self.variables:
            if var not in kwargs.keys():
                raise ValueError(f"Variable: {var} not found in arguments")
            elif isinstance(kwargs[var], str):
                index.append(self.name_to_no[var][kwargs[var]])
            else:
                logging.info(f"Using {var} state as number instead of name.")
                index.append(kwargs[var])

        self.values[tuple(index)] = value

    def assignment(self, index):
        """
        Returns a list of assignments (variable and state) for the corresponding index.

        Parameters
        ----------
        index: list, array-like
            List of indices whose assignment is to be computed

        Returns
        -------
        Full assignments: list
            Returns a list of full assignments of all the variables of the factor.

        Examples
        --------

        """
        index = np.array(index)

        max_possible_index = np.prod(self.cardinality) - 1
        if not all(i <= max_possible_index for i in index):
            raise IndexError("Index greater than max possible index")

        assignments = np.zeros((len(index), len(self.scope())), dtype=int)
        rev_card = self.cardinality[::-1]
        for i, card in enumerate(rev_card):
            assignments[:, i] = index % card
            index = index // card

        assignments = assignments[:, ::-1]

        return [
            [
                (key, self.get_state_names(key, val))
                for key, val in zip(self.variables, values)
            ]
            for values in assignments
        ]

    def identity_factor(self):
        """
        Returns the identity factor.

        Def: The identity factor of a factor has the same scope and cardinality as the original factor,
             but the values for all the assignments is 1. When the identity factor is multiplied with
             the factor it returns the factor itself.

        Returns
        -------
        Identity factor: pgmpy.factors.discrete.DiscreteFactor.
            Returns a factor with all values set to 1.

        Examples
        --------

        """
        return DiscreteFactor(
            variables=self.variables,
            cardinality=self.cardinality,
            values=np.ones(self.values.size),
            state_names=self.state_names,
        )

    def marginalize(self, variables, inplace=True):
        """
        Modifies the factor with marginalized values.

        Parameters
        ----------
        variables: list, array-like
            List of variables over which to marginalize.

        inplace: boolean
            If inplace=True it will modify the factor itself, else would return
            a new factor.

        Returns
        -------
        Marginalized factor: pgmpy.factors.discrete.DiscreteFactor or None
        If inplace=True (default) returns None else returns a new `DiscreteFactor` instance.

        Examples
        --------

        """

        if isinstance(variables, str):
            raise TypeError("variables: Expected type list or array-like, got type str")

        phi = self if inplace else self.copy()

        for var in variables:
            if var not in phi.variables:
                raise ValueError(f"{var} not in scope.")

        var_indexes = [phi.variables.index(var) for var in variables]

        index_to_keep = sorted(set(range(len(self.variables))) - set(var_indexes))
        n_variables = len(self.variables)
        phi.variables = [phi.variables[index] for index in index_to_keep]
        phi.cardinality = phi.cardinality[index_to_keep]
        phi.del_state_names(variables)

        phi.values = np.einsum(phi.values, range(n_variables), index_to_keep)

        if not inplace:
            return phi

    def maximize(self, variables, inplace=True):
        """
        Maximizes the factor with respect to `variables`.

        Parameters
        ----------
        variables: list, array-like
            List of variables with respect to which factor is to be maximized

        inplace: boolean
            If inplace=True it will modify the factor itself, else would return
            a new factor.

        Returns
        -------
        Maximized factor: pgmpy.factors.discrete.DiscreteFactor or None
            If inplace=True (default) returns None else inplace=False returns a
            new `DiscreteFactor` instance.

        Examples
        --------

        """
        if isinstance(variables, str):
            raise TypeError("variables: Expected type list or array-like, got type str")

        phi = self if inplace else self.copy()

        for var in variables:
            if var not in phi.variables:
                raise ValueError(f"{var} not in scope.")

        var_indexes = [phi.variables.index(var) for var in variables]

        index_to_keep = sorted(set(range(len(self.variables))) - set(var_indexes))
        phi.variables = [phi.variables[index] for index in index_to_keep]
        phi.cardinality = phi.cardinality[index_to_keep]
        phi.del_state_names(variables)

        phi.values = np.max(phi.values, axis=tuple(var_indexes))

        if not inplace:
            return phi

    def normalize(self, inplace=True):
        """
        Normalizes the values of factor so that they sum to 1.

        Parameters
        ----------
        inplace: boolean
            If inplace=True it will modify the factor itself, else would return
            a new factor

        Returns
        -------
        Normalized factor: pgmpy.factors.discrete.DiscreteFactor or None
            If inplace=True (default) returns None else returns a new `DiscreteFactor` instance.

        Examples
        --------

        """
        phi = self if inplace else self.copy()

        phi.values = phi.values / phi.values.sum()

        if not inplace:
            return phi

    def reduce(self, values, inplace=True, show_warnings=True):
        """
        Reduces the factor to the context of given variable values. The variables which
        are reduced would be removed from the factor.

        Parameters
        ----------
        values: list, array-like
            A list of tuples of the form (variable_name, variable_state).

        inplace: boolean
            If inplace=True it will modify the factor itself, else would return
            a new factor.

        show_warnings: boolean
            Whether to show warning when state name not found.

        Returns
        -------
        Reduced factor: pgmpy.factors.discrete.DiscreteFactor or None
            If inplace=True (default) returns None else returns a new `DiscreteFactor` instance.

        Examples
        --------
        """
        # Check if values is an array
        if isinstance(values, str):
            raise TypeError("values: Expected type list or array-like, got type str")

        if not all([isinstance(state_tuple, tuple) for state_tuple in values]):
            raise TypeError(
                "values: Expected type list of tuples, get type {type}", type(values[0])
            )

        # Check if all variables in values are in the factor
        for var, _ in values:
            if var not in self.variables:
                raise ValueError(f"The variable: {var} is not in the factor")

        phi = self if inplace else self.copy()

        # Convert the state names to state number. If state name not found treat them as
        # state numbers.
        try:
            values = [
                (var, self.get_state_no(var, state_name)) for var, state_name in values
            ]
        except KeyError:
            if show_warnings:
                warnings.warn(
                    "Found unknown state name. Trying to switch to using all state names as state numbers",
                    UserWarning,
                )

        var_index_to_del = []
        slice_ = [slice(None)] * len(self.variables)
        for var, state in values:
            var_index = phi.variables.index(var)
            slice_[var_index] = state
            var_index_to_del.append(var_index)

        var_index_to_keep = sorted(
            set(range(len(phi.variables))) - set(var_index_to_del)
        )
        # set difference is not guaranteed to maintain ordering
        phi.variables = [phi.variables[index] for index in var_index_to_keep]
        phi.cardinality = phi.cardinality[var_index_to_keep]
        phi.del_state_names([var for var, _ in values])

        phi.values = phi.values[tuple(slice_)]

        if not inplace:
            return phi

    def sum(self, phi1, inplace=True):
        """
        DiscreteFactor sum with `phi1`.

        Parameters
        ----------
        phi1: float or `DiscreteFactor` instance.
            If float, the value is added to each value in the factor.
            DiscreteFactor to be added.

        inplace: boolean
            If inplace=True it will modify the factor itself, else would return
            a new factor.

        Returns
        -------
        Summed factor: pgmpy.factors.discrete.DiscreteFactor or None
            If inplace=True (default) returns None else returns a new `DiscreteFactor` instance.

        Examples
        --------

        """
        phi = self if inplace else self.copy()
        if isinstance(phi1, (int, float)):
            phi.values += phi1
        else:
            phi1 = phi1.copy()

            # modifying phi to add new variables
            extra_vars = set(phi1.variables) - set(phi.variables)
            if extra_vars:
                slice_ = [slice(None)] * len(phi.variables)
                slice_.extend([np.newaxis] * len(extra_vars))
                phi.values = phi.values[tuple(slice_)]

                phi.variables.extend(extra_vars)

                new_var_card = phi1.get_cardinality(extra_vars)
                phi.cardinality = np.append(
                    phi.cardinality, [new_var_card[var] for var in extra_vars]
                )
                phi.add_state_names(phi1)

            # modifying phi1 to add new variables
            extra_vars = set(phi.variables) - set(phi1.variables)
            if extra_vars:
                slice_ = [slice(None)] * len(phi1.variables)
                slice_.extend([np.newaxis] * len(extra_vars))
                phi1.values = phi1.values[tuple(slice_)]

                phi1.variables.extend(extra_vars)
                # No need to modify cardinality as we don't need it.

            # rearranging the axes of phi1 to match phi
            for axis in range(phi.values.ndim):
                exchange_index = phi1.variables.index(phi.variables[axis])
                phi1.variables[axis], phi1.variables[exchange_index] = (
                    phi1.variables[exchange_index],
                    phi1.variables[axis],
                )
                phi1.values = phi1.values.swapaxes(axis, exchange_index)

            phi.values = phi.values + phi1.values

        if not inplace:
            return phi

    def product(self, phi1, inplace=True):
        """
        DiscreteFactor product with `phi1`.

        Parameters
        ----------
        phi1: float or `DiscreteFactor` instance
            If float, all the values are multiplied with `phi1`.
            else if `DiscreteFactor` instance, mutliply based on matching rows.

        inplace: boolean
            If inplace=True it will modify the factor itself, else would return
            a new factor.

        Returns
        -------
        Multiplied factor: pgmpy.factors.discrete.DiscreteFactor or None
            If inplace=True (default) returns None else returns a new `DiscreteFactor` instance.

        Examples
        --------

        """
        phi = self if inplace else self.copy()
        if isinstance(phi1, (int, float)):
            phi.values *= phi1
        else:
            # Compute the new values
            new_variables = list(set(phi.variables).union(phi1.variables))
            var_to_int = {var: index for index, var in enumerate(new_variables)}
            phi.values = np.einsum(
                phi.values,
                [var_to_int[var] for var in phi.variables],
                phi1.values,
                [var_to_int[var] for var in phi1.variables],
                range(len(new_variables)),
            )

            # Compute the new cardinality array
            phi_card = {var: card for var, card in zip(phi.variables, phi.cardinality)}
            phi1_card = {
                var: card for var, card in zip(phi1.variables, phi1.cardinality)
            }
            phi_card.update(phi1_card)
            phi.cardinality = np.array([phi_card[var] for var in new_variables])

            # Set the new variables and state names
            phi.variables = new_variables
            phi.add_state_names(phi1)

        if not inplace:
            return phi

    def divide(self, phi1, inplace=True):
        """
        DiscreteFactor division by `phi1`.

        Parameters
        ----------
        phi1 : `DiscreteFactor` instance
            The denominator for division.

        inplace: boolean
            If inplace=True it will modify the factor itself, else would return
            a new factor.

        Returns
        -------
        Divided factor: pgmpy.factors.discrete.DiscreteFactor or None
            If inplace=True (default) returns None else returns a new `DiscreteFactor` instance.

        Examples
        --------

        """
        phi = self if inplace else self.copy()
        phi1 = phi1.copy()

        if set(phi1.variables) - set(phi.variables):
            raise ValueError("Scope of divisor should be a subset of dividend")

        # Adding extra variables in phi1.
        extra_vars = set(phi.variables) - set(phi1.variables)
        if extra_vars:
            slice_ = [slice(None)] * len(phi1.variables)
            slice_.extend([np.newaxis] * len(extra_vars))
            phi1.values = phi1.values[tuple(slice_)]

            phi1.variables.extend(extra_vars)

        # Rearranging the axes of phi1 to match phi
        for axis in range(phi.values.ndim):
            exchange_index = phi1.variables.index(phi.variables[axis])
            phi1.variables[axis], phi1.variables[exchange_index] = (
                phi1.variables[exchange_index],
                phi1.variables[axis],
            )
            phi1.values = phi1.values.swapaxes(axis, exchange_index)

        phi.values = phi.values / phi1.values

        # If factor division 0/0 = 0 but is undefined for x/0. In pgmpy we are using
        # np.inf to represent x/0 cases.
        phi.values[np.isnan(phi.values)] = 0

        if not inplace:
            return phi

    def sample(self, n):
        """
        Normalizes the factor and samples state combinations from it.

        Parameters
        ----------
        n: int
            No. of samples to return

        Examples
        --------

        """
        phi = self.normalize(inplace=False)
        p = phi.values.ravel()
        indexes = np.random.choice(range(len(p)), size=n, p=p)
        samples = []
        index_to_state = {}
        for index in indexes:
            if index in index_to_state:
                samples.append(index_to_state[index])
            else:
                assignment = self.assignment([index])[0]
                samples.append(assignment)
                index_to_state[index] = assignment

        return pd.DataFrame([{k: v for k, v in s} for s in samples])

    def copy(self):
        """
        Returns a copy of the factor.

        Returns
        -------
        Copy of self: pgmpy.factors.discrete.DiscreteFactor
            A copy of the original discrete factor.

        Examples
        --------

        """
        copy = DiscreteFactor.__new__(self.__class__)
        copy.variables = [*self.variables]
        copy.cardinality = np.array(self.cardinality)
        copy.values = np.array(self.values)
        copy.state_names = self.state_names.copy()
        copy.no_to_name = self.no_to_name.copy()
        copy.name_to_no = self.name_to_no.copy()
        return copy

    def is_valid_cpd(self):
        """
        Checks if the factor's values can be used for a valid CPD.
        """
        return np.allclose(
            self.to_factor()
            .marginalize(self.scope()[:1], inplace=False)
            .values.flatten("C"),
            np.ones(np.product(self.cardinality[:0:-1])),
            atol=0.01,
        )

    def __str__(self):
        return self._str(phi_or_p="phi", tablefmt="grid")

    def _str(self, phi_or_p="phi", tablefmt="grid", print_state_names=True):
        """
        Generate the string from `__str__` method.

        Parameters
        ----------
        phi_or_p: 'phi' | 'p'
                'phi': When used for Factors.
                  'p': When used for CPDs.
        print_state_names: boolean
                If True, the user defined state names are displayed.
        """
        string_header = list(map(str, self.scope()))
        string_header.append(f"{phi_or_p}({','.join(string_header)})")

        value_index = 0
        factor_table = []
        for prob in product(*[range(card) for card in self.cardinality]):
            if self.state_names and print_state_names:
                prob_list = [
                    "{var}({state})".format(
                        var=list(self.variables)[i],
                        state=self.state_names[list(self.variables)[i]][prob[i]],
                    )
                    for i in range(len(self.variables))
                ]
            else:
                prob_list = [
                    f"{list(self.variables)[i]}_{prob[i]}"
                    for i in range(len(self.variables))
                ]

            prob_list.append(self.values.ravel()[value_index])
            factor_table.append(prob_list)
            value_index += 1

        return tabulate(
            factor_table, headers=string_header, tablefmt=tablefmt, floatfmt=".4f"
        )

    def __repr__(self):
        var_card = ", ".join(
            [f"{var}:{card}" for var, card in zip(self.variables, self.cardinality)]
        )
        return f"<DiscreteFactor representing phi({var_card}) at {hex(id(self))}>"

    def __mul__(self, other):
        return self.product(other, inplace=False)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __add__(self, other):
        return self.sum(other, inplace=False)

    def __radd__(self, other):
        return self.__add__(other)

    def __truediv__(self, other):
        return self.divide(other, inplace=False)

    __div__ = __truediv__

    def __eq__(self, other, atol=1e-08):
        """
        Method for checking if two factors are equal.

        Parameters
        ----------
        atol: float
            The maximum allowed difference in values to be considered equal.
        """
        if not (isinstance(self, DiscreteFactor) and isinstance(other, DiscreteFactor)):
            return False

        elif set(self.scope()) != set(other.scope()):
            return False

        else:
            # Change the axis so that the variables are in the same order.
            phi = other.copy()
            if self.variables != phi.variables:
                for axis in range(self.values.ndim):
                    exchange_index = phi.variables.index(self.variables[axis])
                    phi.variables[axis], phi.variables[exchange_index] = (
                        phi.variables[exchange_index],
                        phi.variables[axis],
                    )
                    phi.cardinality[axis], phi.cardinality[exchange_index] = (
                        phi.cardinality[exchange_index],
                        phi.cardinality[axis],
                    )
                    phi.values = phi.values.swapaxes(axis, exchange_index)

            # Check the state names order and match them
            for axis, var in enumerate(self.variables):
                if set(self.state_names[var]) != set(phi.state_names[var]):
                    return False
                elif self.state_names[var] != phi.state_names[var]:
                    ref_index = []
                    for state_name in self.state_names[var]:
                        ref_index.append(phi.state_names[var].index(state_name))

                    slice_ = [slice(None)] * len(self.variables)
                    slice_[axis] = ref_index
                    phi.values = phi.values[tuple(slice_)]

            if phi.values.shape != self.values.shape:
                return False
            elif not np.allclose(phi.values, self.values, atol=atol):
                return False
            elif not all(self.cardinality == phi.cardinality):
                return False
            else:
                return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        variable_hashes = [hash(variable) for variable in self.variables]
        sorted_var_hashes = sorted(variable_hashes)
        state_names_hash = hash(frozenset(self.state_names))
        phi = self.copy()
        for axis in range(phi.values.ndim):
            exchange_index = variable_hashes.index(sorted_var_hashes[axis])
            variable_hashes[axis], variable_hashes[exchange_index] = (
                variable_hashes[exchange_index],
                variable_hashes[axis],
            )
            phi.cardinality[axis], phi.cardinality[exchange_index] = (
                phi.cardinality[exchange_index],
                phi.cardinality[axis],
            )
            phi.values = phi.values.swapaxes(axis, exchange_index)
        return hash(
            str(sorted_var_hashes)
            + str(hash(phi.values.tobytes()))
            + str(hash(phi.cardinality.tobytes()))
            + str(state_names_hash)
        )
