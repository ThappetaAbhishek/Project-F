import math


def calculate(expression):
    """
    Safely evaluates mathematical expressions.
    """

    allowed = {
        "__builtins__": None,
        "sqrt": math.sqrt,
        "pow": pow,
        "abs": abs,
        "round": round,
        "pi": math.pi,
        "e": math.e
    }

    try:
        result = eval(expression, allowed, {})
        return str(result)

    except Exception:
        return None