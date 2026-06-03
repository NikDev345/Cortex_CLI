import ast
import operator

OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg
}


def evaluate(node):
    if isinstance(node, ast.Num):
        return node.n

    if isinstance(node, ast.BinOp):
        return OPERATORS[type(node.op)](
            evaluate(node.left),
            evaluate(node.right)
        )

    if isinstance(node, ast.UnaryOp):
        return OPERATORS[type(node.op)](
            evaluate(node.operand)
        )

    raise TypeError("Unsupported operation")


def calculate(expression):
    try:
        node = ast.parse(expression, mode="eval").body
        return evaluate(node)

    except Exception:
        return "Invalid mathematical expression"