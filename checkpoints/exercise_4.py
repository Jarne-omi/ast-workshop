"""Exercise 4: https://stefaniemolin.com/ast-workshop/#/exercise-4

Create an ast.NodeTransformer to add placeholder messages to all assert calls that don't have them. 
We did this earlier with ast.walk(), and this will look very similar.
Don't forget to return the node after visiting it, or it will be removed from the tree.

Reminder: We want to visit the ast.Assert nodes and check for the presence of a message (available in the msg attribute). 
You can review the structure of the node with ast-explore as follows:

$ ast-explore snippets/assert.py --types Assert
"""


import ast
from pathlib import Path

class AssertTransformer(ast.NodeTransformer):
    def visit_Assert(self, node: ast.Assert) -> ast.AST:
        node = self.generic_visit(node)  # Visit child nodes first
        
        if node.msg is None:
            node.msg = ast.Constant(value="TODO: Add assert message")
            node = ast.fix_missing_locations(node)  # Fix location info for the new node
        return node


if __name__ == "__main__":
    with open('snippets/assert.py', 'r') as f:
        source = f.read()

    tree = ast.parse(source)
    transformer = AssertTransformer()
    transformed_tree = transformer.visit(tree)

    # Optionally, you can unparse the modified AST back to source code
    modified_source = ast.unparse(transformed_tree)
    print(modified_source)
    Path("snippets/assert_transformed.py").write_text(ast.unparse(transformed_tree))
