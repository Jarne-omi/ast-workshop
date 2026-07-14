"""Exercise 3: https://stefaniemolin.com/ast-workshop/#/exercise-3

Create a GenericExceptionVisitor class that detects both bare except blocks and the usage of generic Exceptions:

```python
try:
    del x['non_existent_key']
except:  # bare except
    raise Exception('No such key')  # generic Exception
```

Tip: Start by exploring ast.ExceptHandler and ast.Raise nodes in the generic_exception.py snippet, which has multiple variations of what we want to detect:

$ ast-explore snippets/generic_exception.py --interactive \
    --types ExceptHandler Raise

Bonus: If you have time, use the ast.get_source_segment() function to print any problematic code you detect.
"""

import ast

class GenericExceptionVisitor(ast.NodeVisitor):
    def __init__(self, source_code: str) -> None:
        self.bare_except_count = 0
        self.generic_exception_count = 0
        self.source_code = source_code
        self.tree = ast.parse(source_code)

    def visit_ExceptHandler(self, node: ast.ExceptHandler) -> None:
        match node.type:
            case None:
                print(f"Bare except detected at line {node.lineno}")
                self.bare_except_count += 1
            case ast.Name(id='Exception'):
                print(f"Generic Exception detected at line {node.lineno}")
                self.generic_exception_count += 1

        self.generic_visit(node)


    def visit_Raise(self, node: ast.Raise) -> None:
        match node.exc:
            case (ast.Call(func=ast.Name(id='Exception')) |
                 ast.Name(id='Exception')):
                print(f"Generic Exception detected at line {node.lineno}")
                self.generic_exception_count += 1

        self.generic_visit(node)

    def report(self) -> None:
        print(f"Total bare except blocks: {self.bare_except_count}")
        print(f"Total generic Exception usages: {self.generic_exception_count}")

    def run(self):
        self.visit(self.tree)
        self.report()

if __name__ == "__main__":
    with open('snippets/generic_exception.py', 'r') as f:
        source_code = f.read()

    visitor = GenericExceptionVisitor(source_code)
    visitor.run()
