import numpy as np
from scipy.special import comb
import math

# TODO: Docstrings
class NeutrosophicNumber(object):
    '''
    Neutrosophic numbers are special numbers
    that have 'deterministic' and 'indeterministic'
    parts. Such a number is written a+bI where a is the
    deterministic part and b is the indeterministic part.

    Note: I^n = I for any natural number n.

    Neutrosophic numbers form a commutative ring with addition
    and multiplication.
    '''
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, rhs):
        '''
        This method defines addition of
        neutrosophic numbers using operator overloading
        of the '+' symbol.

        (a+bI) + (c+dI) = (a+c) + (b+d)I
        '''
        if isinstance(rhs, NeutrosophicNumber):
            return NeutrosophicNumber(self.a + rhs.a, self.b + rhs.b)
        else:
            return NeutrosophicNumber(self.a + rhs, self.b)

    def __radd__(self, lhs):
        '''
        This method defines addition of
        neutrosophic numbers using operator overloading
        of the '+' symbol.

        (a+bI) + (c+dI) = (a+c) + (b+d)I
        '''
        if isinstance(lhs, NeutrosophicNumber):
            return NeutrosophicNumber(lhs.a + self.a, lhs.b + self.b)
        else:
            return NeutrosophicNumber(lhs + self.a, self.b)

    def __sub__(self, rhs):
        '''
        This method defines subtraction of
        neutrosophic numbers using operator overloading
        of the '-' symbol.

        (a+bI) - (c+dI) = (a-c) + (b-d)I
        '''
        if isinstance(rhs, NeutrosophicNumber):
            return NeutrosophicNumber(self.a - rhs.a, self.b - rhs.b)
        else:
            return NeutrosophicNumber(self.a - rhs, self.b)

    def __rsub__(self, lhs):
        '''
        This method defines subtraction of
        neutrosophic numbers using operator overloading
        of the '-' symbol.

        (a+bI) - (c+dI) = (a-c) + (b-d)I
        '''
        if isinstance(lhs, NeutrosophicNumber):
            return NeutrosophicNumber(lhs.a - self.a, lhs.b - self.b)
        else:
            return NeutrosophicNumber(lhs - self.a, self.b)

    def __mul__(self, rhs):
        '''
        This method defines scalar multiplication of
        neutrosophic numbers using operator overloading
        of the '*' symbol.

        (a+bI) * (c+dI) = (ac) + (ad + bc + bd)I
        '''
        if isinstance(rhs, NeutrosophicNumber):
            return NeutrosophicNumber(self.a * rhs.a, self.a * rhs.b + self.b * rhs.a + self.b * rhs.b)
        else:
            return NeutrosophicNumber(self.a * rhs, self.b * rhs)

    def __rmul__(self, lhs):
        '''
        This method defines scalar multiplication of
        neutrosophic numbers using operator overloading
        of the '*' symbol.

        (a+bI) * (c+dI) = (ac) + (ad + bc + bd)I
        '''
        if isinstance(lhs, NeutrosophicNumber):
            return NeutrosophicNumber(lhs.a * self.a, lhs.b * self.a + lhs.a * self.b + lhs.b * self.b)
        else:
            return NeutrosophicNumber(lhs * self.a, lhs * self.b)

    def __truediv__(self, rhs):
        if isinstance(rhs, NeutrosophicNumber):
            return NeutrosophicNumber(self.a / rhs.a, (rhs.a * self.b - self.a * rhs.b) / (rhs.a * (rhs.a + rhs.b)))
        else:
            return NeutrosophicNumber(self.a / rhs, self.b / rhs)

    def __pow__(self, rhs):
        if rhs == 0:
            return NeutrosophicNumber(1, 0)
        elif rhs == 1:
            return NeutrosophicNumber(self.a, self.b)
        elif int(rhs) == rhs:
            first_term = NeutrosophicNumber(self.a ** rhs, 0)
            other_terms = np.sum([NeutrosophicNumber(0, comb(rhs, i, exact=True) * self.a ** (rhs-i) * self.b ** i) for i in range(1, rhs+1)])
            return  first_term + other_terms
        else:
            return nexp(rhs * nln(self))

    def __abs__(self):
        '''
        Takes the magnitude of a neutrosophic number to be a+bI
        to be (a^2 + b^2)^0.5, which may not be standard.
        '''
        return (self.a**2 + self.b**2)**0.5

    def __eq__(self, rhs):
        '''
        Two neutrosophic numbers are equal if their
        deterministic parts equal and their indeterministic
        parts equal.
        '''
        return self.a == rhs.a and self.b == rhs.b

    def __ne__(self, rhs):
        '''
        The negation of two neutrosophic numbers
        being equal.
        '''
        return not self.__eq__(rhs)

    def __str__(self):
        if isinstance(self.b, complex):
            return f'{self.a}+{self.b}I'
        elif self.b >= 0:
            return f'{self.a}+{self.b}I'
        else:
            return f'{self.a}{self.b}I'

    def __repr__(self):
        if isinstance(self.b, complex):
            return f'{self.a}+{self.b}I'
        elif self.b >= 0:
            return f'{self.a}+{self.b}I'
        else:
            return f'{self.a}{self.b}I'

def neutrolize_vector(X, deter=True):
    '''
    Only for 1D arrays right now.
    '''
    assert len(X.shape) == 1
    Z = np.zeros(X.shape, dtype=NeutrosophicNumber)
    if deter:
        for i in range(X.shape[0]):
            Z[i] = Z[i] + NeutrosophicNumber(X[i],0)
    else:
        for i in range(X.shape[0]):
            Z[i] = Z[i] + NeutrosophicNumber(0,X[i])
    return Z

# TODO: Docstrings
def nexp(x, order=10):
    '''
    Neutrosophic exponential function approximated by its Maclaurin series.
    '''
    return np.sum([(x ** k) / math.factorial(k) for k in range(order)])

# TODO: Docstrings
def nsin(x, order=10):
    '''
    Neutrosophic sine function approximated by its Maclaurin series.
    '''
    return np.sum([(-1)**k * (x ** (2*k+1)) / math.factorial(2*k+1) for k in range(order)])

# TODO: Docstrings
def nln(x, order=10):
    '''
    Neutrosophic ln function approximated by a series based on the area
    hyperbolic tangent function.
    '''
    return 2 * np.sum([((x-1)/(x+1))**(2*k+1) / (2*k+1) for k in range(order)])
