
# Declaring a constant `PI` of type `float` with a value of `3.141592653589793`.
from typing import Final

PI: Final[float] = 3.141592653589793

# Declaring a constant `e` of type `float` with a value of `2.718281828459045`.
e: Final[float] = 2.718281828459045


def capitalSigma() -> str:
    """
    Capital Sigma
    :return: The string '∑'
    """
    return '∑'


def capitalPi() -> str:
    """
    Capital Pi
    :return: The string 'Π'
    """
    return 'Π'


def exp(x: int) -> float:
    """
    Compute the exponential of x

    :param x: the exponent
    :type x: int
    :return: The value of e to the power of x.
    """
    if x == 0:
        return 1
    else:
        return e*exp(x-1)


def pow(a: float, x: int) -> float:
    """
    Compute the result of the base a, to the power of x.

    :param a: the base of the power
    :type a: float
    :param x: the exponent
    :type x: int
    :return: The value of a to the power of x.
    """
    if x == 0:
        return 1
    else:
        return a*pow(a, x-1)


def factorial(x: int) -> int:
    """
    Given an integer x, return the factorial of x

    :param x: The number to calculate the factorial of.
    :type x: int
    :return: The factorial of x.
    """
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)


def combinations(n: int, r: int) -> int:
    """
    The number of ways to choose a sample of r elements from a set of n distinct 
    objects where order does not matter and replacements are not allowed.

    :param n: the number of items in the list
    :type n: int
    :param r: The number of elements to choose from n: The total number of elements
    :type r: int
    :return: The number of combinations of n objects taken r at a time.
    """
    return factorial(n) // (factorial(n-r) * factorial(r))


def permutations(n: int, r: int) -> int:
    """
    Given a number n, return the number of ways to permute n objects

    :param n: the number of items in the list
    :type n: int
    :param r: The number of elements to choose from n: The total number of elements
    :type r: int
    :return: The number of permutations of n objects taken r at a time.
    """
    return factorial(n) // factorial(n-r)


def summation(a: int, i: int, n: int) -> int:
    """
    Given an integer a, return the sum of a from i to n

    :param a: the first number in the summation
    :type a: int
    :param i: the starting index of the summation
    :type i: int
    :param n: The number of terms to be summed
    :type n: int
    :return: The sum of the first n integers.
    """
    if i > n:  # Incorrect usage
        return None
    if i == n:  # Base Case
        return a
    else:       # Continue recursion
        return a + summation(a, i+1, n)
