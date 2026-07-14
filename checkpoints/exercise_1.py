"""Exercise 1: https://stefaniemolin.com/ast-workshop/#/exercise-1

1. Try passing source code that has a SyntaxError into the ast.parse() function. What happens?
2. What about if the code has an error unrelated to syntax, for instance, a NameError or TypeError?
"""

import ast

print(ast.parse("x+"))  # This will raise a SyntaxError
"""SyntaxError: invalid syntax"""

print(ast.parse("print(x)"))  # This will not raise a SyntaxError, but if you try to execute the code, it will raise a NameError because 'x' is not defined.
"""This parses"""

x = "hello"
y = 15
print(ast.parse("print(x + y)"))  # This will not raise a SyntaxError, but if you try to execute the code, it will raise a TypeError because you cannot add a string and an integer.
"""This parses"""
