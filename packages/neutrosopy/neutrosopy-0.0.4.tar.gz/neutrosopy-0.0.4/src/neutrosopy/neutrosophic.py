"""
The neutrosophic_numbers module provides functionality for working with neutrosophic numbers, a special type of numbers that combine 'deterministic' and 'indeterministic' parts. A neutrosophic number is represented as a+bI, where 'a' is the deterministic part and 'b' is the indeterministic part.

Neutrosophic numbers have properties such as I^n = I for any natural number n and form a commutative ring with addition and multiplication operations. This module allows you to create, manipulate, and perform common mathematical operations on neutrosophic numbers.

Neutrosophic Numbers:
---------------------
- Neutrosophic numbers are a mathematical concept that combines deterministic and indeterministic parts.
- They are represented as a+bI, where 'a' is the deterministic part and 'b' is the indeterministic part.

Functionality:
--------------
- The module implements the NeutrosophicNumber class, which represents a neutrosophic number.
- It provides various methods for performing mathematical operations on neutrosophic numbers, such as addition, subtraction, multiplication, division, exponentiation, and computing the magnitude.
- The NeutrosophicNumber class overloads operators for convenient usage of mathematical operations.
- It also includes methods for comparing neutrosophic numbers for equality and inequality.

Examples:
---------
>>> n1 = NeutrosophicNumber(3, 4)  # Represents the number 3 + 4I
>>> n2 = NeutrosophicNumber(2, -1)  # Represents the number 2 - I

# Addition
>>> result_add = n1 + n2  # Adds the two neutrosophic numbers: (3 + 4I) + (2 - I) = 5 + 3I

# Subtraction
>>> result_sub = n1 - n2  # Subtracts the two neutrosophic numbers: (3 + 4I) - (2 - I) = 1 + 5I

# Scalar multiplication
>>> scalar = 2
>>> result_mul = n1 * scalar  # Multiplies the neutrosophic number by a scalar: (3 + 4I) * 2 = 6 + 8I

# Division
>>> result_div = n1 / n2  # Divides the neutrosophic numbers: (3 + 4I) / (2 - I) = 2.0769 + 0.9231I

# Exponentiation
>>> exponent = 2
>>> result_pow = n1 ** exponent  # Raises the neutrosophic number to a power: (3 + 4I) ** 2 = -7 + 24I

# Magnitude (absolute value)
>>> magnitude = abs(n1)  # Computes the magnitude of the neutrosophic number: |(3 + 4I)| = 5

# Equality comparison
>>> is_equal = n1 == n2  # Checks if the neutrosophic numbers are equal
"""


import math

import numpy as np
from scipy.special import comb


class NeutrosophicNumber:
    """Algebraic neutrosophic number.

    Neutrosophic numbers are a special type of numbers that consist of 'deterministic' and 'indeterministic'
    parts. A neutrosophic number is represented as a+bI, where 'a' is the deterministic part and 'b' is the
    indeterministic part.

    Properties
    ----------
    - Neutrosophic numbers follow the property I^n = I for any natural number n.
    - They form a commutative ring with addition and multiplication operations.

    Methods
    -------
    __init__(a, b)
        Initializes a neutrosophic number with the given deterministic and indeterministic parts.
    __add__(rhs)
        Defines addition of neutrosophic numbers using the '+' operator.
    __sub__(rhs)
        Defines subtraction of neutrosophic numbers using the '-' operator.
    __mul__(rhs)
        Defines scalar multiplication of neutrosophic numbers using the '*' operator.
    __truediv__(rhs)
        Defines division of neutrosophic numbers using the '/' operator.
    __pow__(rhs)
        Defines exponentiation of neutrosophic numbers using the '**' operator.
    __abs__()
        Computes the magnitude (absolute value) of a neutrosophic number.
    __eq__(rhs)
        Checks if two neutrosophic numbers are equal.
    __ne__(rhs)
        Checks if two neutrosophic numbers are not equal.
    __str__()
        Returns a string representation of the neutrosophic number.
    __repr__()
        Returns a string representation of the neutrosophic number.

    Examples
    --------
    >>> n1 = NeutrosophicNumber(3, 4)  # Represents the number 3 + 4I
    >>> n2 = NeutrosophicNumber(2, -1)  # Represents the number 2 - I

    # Addition
    >>> result_add = n1 + n2  # Adds the two neutrosophic numbers: (3 + 4I) + (2 - I) = 5 + 3I

    # Subtraction
    >>> result_sub = n1 - n2  # Subtracts the two neutrosophic numbers: (3 + 4I) - (2 - I) = 1 + 5I

    # Scalar multiplication
    >>> scalar = 2
    >>> result_mul = n1 * scalar  # Multiplies the neutrosophic number by a scalar: (3 + 4I) * 2 = 6 + 8I

    # Division
    >>> result_div = n1 / n2  # Divides the neutrosophic numbers: (3 + 4I) / (2 - I) = 2.0769 + 0.9231I

    # Exponentiation
    >>> exponent = 2
    >>> result_pow = n1 ** exponent  # Raises the neutrosophic number to a power: (3 + 4I) ** 2 = -7 + 24I

    # Magnitude (absolute value)
    >>> magnitude = abs(n1)  # Computes the magnitude of the neutrosophic number: |(3 + 4I)| = 5

    # Equality comparison
    >>> is_equal = n1 == n2  # Checks if the neutrosophic numbers are equal
    """

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, rhs):
        """
        This method defines addition of
        neutrosophic numbers using operator overloading
        of the '+' symbol.

        (a+bI) + (c+dI) = (a+c) + (b+d)I
        """
        if isinstance(rhs, NeutrosophicNumber):
            return NeutrosophicNumber(self.a + rhs.a, self.b + rhs.b)
        else:
            return NeutrosophicNumber(self.a + rhs, self.b)

    def __radd__(self, lhs):
        """
        This method defines addition of
        neutrosophic numbers using operator overloading
        of the '+' symbol.

        (a+bI) + (c+dI) = (a+c) + (b+d)I
        """
        if isinstance(lhs, NeutrosophicNumber):
            return NeutrosophicNumber(lhs.a + self.a, lhs.b + self.b)
        else:
            return NeutrosophicNumber(lhs + self.a, self.b)

    def __sub__(self, rhs):
        """
        This method defines subtraction of
        neutrosophic numbers using operator overloading
        of the '-' symbol.

        (a+bI) - (c+dI) = (a-c) + (b-d)I
        """
        if isinstance(rhs, NeutrosophicNumber):
            return NeutrosophicNumber(self.a - rhs.a, self.b - rhs.b)
        else:
            return NeutrosophicNumber(self.a - rhs, self.b)

    def __rsub__(self, lhs):
        """
        This method defines subtraction of
        neutrosophic numbers using operator overloading
        of the '-' symbol.

        (a+bI) - (c+dI) = (a-c) + (b-d)I
        """
        if isinstance(lhs, NeutrosophicNumber):
            return NeutrosophicNumber(lhs.a - self.a, lhs.b - self.b)
        else:
            return NeutrosophicNumber(lhs - self.a, self.b)

    def __mul__(self, rhs):
        """
        This method defines scalar multiplication of
        neutrosophic numbers using operator overloading
        of the '*' symbol.

        (a+bI) * (c+dI) = (ac) + (ad + bc + bd)I
        """
        if isinstance(rhs, NeutrosophicNumber):
            return NeutrosophicNumber(
                self.a * rhs.a, self.a * rhs.b + self.b * rhs.a + self.b * rhs.b
            )
        else:
            return NeutrosophicNumber(self.a * rhs, self.b * rhs)

    def __rmul__(self, lhs):
        """
        This method defines scalar multiplication of
        neutrosophic numbers using operator overloading
        of the '*' symbol.

        (a+bI) * (c+dI) = (ac) + (ad + bc + bd)I
        """
        if isinstance(lhs, NeutrosophicNumber):
            return NeutrosophicNumber(
                lhs.a * self.a, lhs.b * self.a + lhs.a * self.b + lhs.b * self.b
            )
        else:
            return NeutrosophicNumber(lhs * self.a, lhs * self.b)

    def __truediv__(self, rhs):
        if isinstance(rhs, NeutrosophicNumber):
            return NeutrosophicNumber(
                self.a / rhs.a,
                (rhs.a * self.b - self.a * rhs.b) / (rhs.a * (rhs.a + rhs.b)),
            )
        else:
            return NeutrosophicNumber(self.a / rhs, self.b / rhs)

    def __pow__(self, rhs):
        if rhs == 0:
            return NeutrosophicNumber(1, 0)
        elif rhs == 1:
            return NeutrosophicNumber(self.a, self.b)
        elif int(rhs) == rhs:
            first_term = NeutrosophicNumber(self.a**rhs, 0)
            other_terms = np.sum(
                [
                    NeutrosophicNumber(
                        0, comb(rhs, i, exact=True) * self.a ** (rhs - i) * self.b**i
                    )
                    for i in range(1, rhs + 1)
                ]
            )
            return first_term + other_terms
        else:
            return nexp(rhs * nln(self))

    def __abs__(self):
        """
        Takes the magnitude of a neutrosophic number to be a+bI
        to be (a^2 + b^2)^0.5, which may not be standard.
        """
        return (self.a**2 + self.b**2) ** 0.5

    def __eq__(self, rhs):
        """
        Two neutrosophic numbers are equal if their
        deterministic parts equal and their indeterministic
        parts equal.
        """
        return self.a == rhs.a and self.b == rhs.b

    def __ne__(self, rhs):
        """
        The negation of two neutrosophic numbers
        being equal.
        """
        return not self.__eq__(rhs)

    def __str__(self):
        if isinstance(self.b, complex):
            return f"{self.a}+{self.b}I"
        elif self.b >= 0:
            return f"{self.a}+{self.b}I"
        else:
            return f"{self.a}{self.b}I"

    def __repr__(self):
        if isinstance(self.b, complex):
            return f"{self.a}+{self.b}I"
        elif self.b >= 0:
            return f"{self.a}+{self.b}I"
        else:
            return f"{self.a}{self.b}I"


def neutrolize_vector(X, deter=True):
    """
    Convert a 1D array into a neutrosophic vector.

    Parameters:
    -----------
    X : numpy.ndarray
        The 1D array to be converted into a neutrosophic vector.

    deter : bool, optional
        Specifies whether to consider the elements of 'X' as the deterministic part of the neutrosophic vector.
        If True, the elements of 'X' are considered as the deterministic part (default).
        If False, the elements of 'X' are considered as the indeterministic part.

    Returns:
    --------
    Z : numpy.ndarray
        A 1D array of neutrosophic numbers representing the neutrosophic vector.

    Raises:
    -------
    AssertionError:
        If the input array 'X' is not one-dimensional.

    Notes:
    ------
    - The function assumes that 'X' is a 1D array.
    - The function returns a neutrosophic vector where each element of 'X' is converted into a neutrosophic number.
    - If 'deter' is True, each element of 'X' is treated as the deterministic part of the neutrosophic number.
    - If 'deter' is False, each element of 'X' is treated as the indeterministic part of the neutrosophic number.
    - The neutrosophic numbers are represented using the NeutrosophicNumber class.

    Examples:
    ---------
    >>> X = np.array([1, 2, 3])
    >>> neutrolize_vector(X)
    array([1+0I, 2+0I, 3+0I])

    >>> Y = np.array([0.1, 0.2, 0.3])
    >>> neutrolize_vector(Y, deter=False)
    array([0+0.1I, 0+0.2I, 0+0.3I])
    """
    assert len(X.shape) == 1
    Z = np.zeros(X.shape, dtype=NeutrosophicNumber)
    if deter:
        for i in range(X.shape[0]):
            Z[i] = Z[i] + NeutrosophicNumber(X[i], 0)
    else:
        for i in range(X.shape[0]):
            Z[i] = Z[i] + NeutrosophicNumber(0, X[i])
    return Z


def nexp(x, order=10):
    """
    Compute the neutrosophic exponential function approximation using its Maclaurin series.

    Parameters:
    -----------
    x : numeric
        The value at which to evaluate the neutrosophic exponential function.

    order : int, optional
        The order of the Maclaurin series used for the approximation.
        Default is 10.

    Returns:
    --------
    NeutrosophicNumber
        A neutrosophic number representing the approximation of the neutrosophic exponential function.

    Notes:
    ------
    - The neutrosophic exponential function is approximated using its Maclaurin series.
    - The Maclaurin series is truncated at the specified 'order'.
    - The function computes the sum of the terms in the Maclaurin series approximation.
    - The resulting sum is returned as a neutrosophic number.
    - The neutrosophic number is represented using the NeutrosophicNumber class.

    Examples:
    ---------
    >>> nexp(1)
    2+1I

    >>> nexp(2, order=5)
    7+4.333333333333333I
    """
    return np.sum([(x**k) / math.factorial(k) for k in range(order)])


def nsin(x, order=10):
    """
    Compute the neutrosophic sine function approximation using its Maclaurin series.

    Parameters:
    -----------
    x : numeric
        The value at which to evaluate the neutrosophic sine function.

    order : int, optional
        The order of the Maclaurin series used for the approximation.
        Default is 10.

    Returns:
    --------
    NeutrosophicNumber
        A neutrosophic number representing the approximation of the neutrosophic sine function.

    Notes:
    ------
    - The neutrosophic sine function is approximated using its Maclaurin series.
    - The Maclaurin series is truncated at the specified 'order'.
    - The function computes the sum of the terms in the Maclaurin series approximation.
    - The resulting sum is returned as a neutrosophic number.
    - The neutrosophic number is represented using the NeutrosophicNumber class.

    Examples:
    ---------
    >>> nsin(0)
    0+0I

    >>> nsin(1)
    1.1666666666666665+1.1752011936438014I

    >>> nsin(2, order=5)
    -0.9333333333333332+3.9933992677987827I
    """
    return np.sum(
        [
            (-1) ** k * (x ** (2 * k + 1)) / math.factorial(2 * k + 1)
            for k in range(order)
        ]
    )


def nln(x, order=10):
    """
    Compute the neutrosophic natural logarithm function approximation using
    a series based on the area hyperbolic tangent function.

    Parameters:
    -----------
    x : numeric
        The value at which to evaluate the neutrosophic natural logarithm function.

    order : int, optional
        The order of the series used for the approximation.
        Default is 10.

    Returns:
    --------
    NeutrosophicNumber
        A neutrosophic number representing the approximation of the neutrosophic natural logarithm function.

    Notes:
    ------
    - The neutrosophic natural logarithm function is approximated using a series based on the area hyperbolic tangent function.
    - The series is truncated at the specified 'order'.
    - The function computes the sum of the terms in the series approximation.
    - The resulting sum is multiplied by 2 and returned as a neutrosophic number.
    - The neutrosophic number is represented using the NeutrosophicNumber class.

    Examples:
    ---------
    >>> nln(1)
    0+0I

    >>> nln(2)
    1.0986122886681098+1.5707963267948966I

    >>> nln(3, order=5)
    1.1752011936438014+1.5040773967762742I
    """
    return 2 * np.sum(
        [((x - 1) / (x + 1)) ** (2 * k + 1) / (2 * k + 1) for k in range(order)]
    )
