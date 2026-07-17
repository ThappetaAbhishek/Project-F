import re

from tools.wiki import get_summary


def can_handle(message):
    """
    Detect factual questions that Wikipedia can answer.
    """

    text = message.lower().strip()

    patterns = [
        "who is",
        "what is",
        "tell me about",
        "define",
        "explain"
    ]

    return any(text.startswith(pattern) for pattern in patterns)


def extract_query(text):

    prefixes = [
        "Who is",
        "What is",
        "Tell me about",
        "Define",
        "Explain",

        "who is",
        "what is",
        "tell me about",
        "define",
        "explain"
    ]

    query = text

    for prefix in prefixes:

        if text.startswith(prefix):

            query = text[len(prefix):].strip()

            break

    # Stop at common connectors
    separators = [
        " and ",
        " latest ",
        " news ",
        "?",
        ","
    ]

    lowest = len(query)

    lower = query.lower()

    for sep in separators:

        pos = lower.find(sep)

        if pos != -1 and pos < lowest:
            lowest = pos

    query = query[:lowest].strip()

    # Remove extra punctuation
    query = re.sub(r"[?.!,]+$", "", query).strip()

    return query


def handle(message):

    query = extract_query(message)

    if not query:
        return "Please specify a topic."

    result = get_summary(query)

    if "error" in result:
        return result["error"]

    return f"""📖 {result['title']}

{result['summary']}

🔗 {result['url']}
"""