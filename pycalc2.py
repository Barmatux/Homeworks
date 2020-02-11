from __future__ import division, print_function
from textwrap import dedent
import math
import operator as op
from collections import OrderedDict
import re
import doctest

# Regex to split into numbers and operators
TOKEN_SPLITTER = re.compile("""
    \s*                # Ignore leading whitespace
    (                  # Group the result, which is either ...
     (?<!\d)-?           # A possibly negative (but not the operator minus)
     \d+                 # number
     (?:\.\d+)?          # with optional fraction part
    |                  # ... or alternate group of ...
      (?://|\*\*)        # Non-capturing single operator
      |(?:[+-/*^])       # or two-character operator group
    )                  # ... end of group
    \s*                # Ignore trailing whitespace
    """, re.X)

# Define legal operators in precedence order
OPERATORS = OrderedDict([
    # '(' and ')' are not implemented yet!, and needs special care
    ('^', math.pow),
    ('**', math.pow),
    ('*', op.mul),
    ('/', op.truediv),
    ('//', op.floordiv),
    ('+', op.add),
    ('-', op.sub),
])


def tokenizer(expression):
    """Splits expression into numbers and operator tokens, and returns list.

    The expression can contain numbers with or without decimal part, and
    various operators. In general spaces are allowed, but to be able to
    correctly determine negative numbers, there can be no space inbetween
    the '-' and the number, i.e. "-5" is legal, but "- 5" is tokenized as
    the minus operator, and the number 5.

    Here are some various expressions with resulting token lists:
      >>> tokenizer("10-2^3*5/2--5")
      [10, '-', 2, '^', 3, '*', 5, '/', 2, '-', -5]

      >>> tokenizer("1*2.0/3**4+5-6")
      [1, '*', 2.0, '/', 3, '**', 4, '+', 5, '-', 6]

      >>> tokenizer("  2  * -3 + 6 /3--5       ")
      [2, '*', -3, '+', 6, '/', 3, '-', -5]
    """


    def _numberify(token):
        """Turn token into int or float, if possible."""

        try:
            # Check if it is an int and return it
            return int(token)

        except ValueError:
            # Not an int, is it possibly a float?
            try:
                return float(token)

            except ValueError:
                # Not a number, return operator as is
                return token


    ## Split into numbers and operators, and make number strings into numbers
    return list(map(_numberify, TOKEN_SPLITTER.findall(expression)))

def calculate(expression):
    if isinstance(expression, str):
        token_list = tokenizer(expression)

    else:
        token_list = expression

    # Loop through all operators in precedented order, applying each of them
    for operator in OPERATORS:

        # Apply the operator and reduce the two surrounding elements
        # using this operation
        while True:

            # Find operator in list, and break out of loop if not found
            try:
                idx = token_list.index(operator)
            except ValueError:
                break

            # Operator found, calculate and reduce
            if idx == 0 or idx == len(token_list):
                raise ValueError("No numbers to perform operation on")

            operation_slice = slice(idx - 1, idx + 2)
            operands = token_list[operation_slice]

            # Here is the magic: It replaces a slice of the list, with the
            # calculated result of the operation applied to operands
            token_list[operation_slice] = [OPERATORS[operator](operands[0], operands[2])]

        # If the token list only has one element left, we're done calculating
        # and can return the result
        if len(token_list) == 1:
            return token_list[0]

    # If however we've exhausted all operators, and the list has multiple
    # elements there is an error in the original expression.
    raise ValueError("Couldn't calculate all of it! Remaining tokens: {}".format(token_list))


def main():

    print(dedent("""
        Welcome to an interactive calculator!

        Enter your expression and hit enter to calculate it. The calculator
        supports the normal operations, powers and floor division. Currrently
        parenthesis are not allowed. Enter 'quit' as the expression when you
        want to end the calculator."""))

    while True:
        expression = input("Type in expression (or 'quit'): ").lower()

        if expression == 'quit':
            break

        print("    {} = {}".format(expression, calculate(expression)))


if __name__ == '__main__':
    doctest.testmod()
    main()