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


def handle(message):

    text = message.strip()

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

    if not query:
        return "Please specify a topic."

    result = get_summary(query)

    if "error" in result:
        return result["error"]

    return f"""📖 {result['title']}

{result['summary']}

🔗 {result['url']}
"""