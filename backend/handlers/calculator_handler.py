import re

from tools.calculator import calculate


def can_handle(message):

    text = message.strip()

    # Accept digits, spaces and math operators
    pattern = r"^[0-9+\-*/().,\s^%]+$"

    if re.fullmatch(pattern, text):
        return True

    # Accept functions like sqrt(...)
    if text.lower().startswith("sqrt("):
        return True

    if text.lower().startswith("round("):
        return True

    if text.lower().startswith("abs("):
        return True

    if text.lower().startswith("pow("):
        return True

    return False


def handle(message):

    expression = message.replace("^", "**")

    result = calculate(expression)

    if result is None:
        return "Invalid mathematical expression."

    return result