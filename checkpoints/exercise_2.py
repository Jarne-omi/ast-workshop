"""Exercise 2: https://stefaniemolin.com/ast-workshop/#/exercise-2

Use the ast.walk() function and the ast.get_docstring() function to traverse the AST for the greet.py snippet 
and report any items that are missing docstrings.
"""

import ast

with open('snippets/greet.py', 'r') as f:
    source = f.read()

missing_docstrings = []
for node in ast.walk(ast.parse(source)):
    if isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.Module, ast.AsyncFunctionDef)) and ast.get_docstring(node) is None:
        missing_docstrings.append(node)

print("Items missing docstrings:")
for node in missing_docstrings:
    print(f"- {type(node).__name__} at line {getattr(node, 'lineno', 'N/A')} and module {getattr(node, 'name', 'module')}")
