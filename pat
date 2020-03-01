import re
from operator import *


symbol_table = {}

token_pattern  = re.compile("(?:(\d*\.\d*)|(\d)|(\w+)|(\*\*|.))")

operator_table = {'+': add, '-': sub, '*': mul, '/': truediv, '%': mod, '^' : pow, '>': lt, '<': le, '=': eq}

