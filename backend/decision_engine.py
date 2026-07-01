"""
Project F Decision Engine

This module decides which handler should answer
before the router starts checking every handler.
"""


def decide(message):

    text = message.lower().strip()

    # ---------------- Weather ----------------

    weather_words = [
        "weather",
        "temperature",
        "forecast",
        "humidity",
        "wind"
    ]

    if any(word in text for word in weather_words):
        return "weather"

    # ---------------- News ----------------

    news_words = [
        "latest",
        "news",
        "headline",
        "breaking"
    ]

    if any(word in text for word in news_words):
        return "news"

    # ---------------- Wikipedia ----------------

    wiki_words = [
        "who is",
        "what is",
        "tell me about",
        "define",
        "explain"
    ]

    if any(text.startswith(word) for word in wiki_words):
        return "wiki"

    # ---------------- Search ----------------

    search_words = [
        "/search",
        "search",
        "search for",
        "find",
        "look up"
    ]

    if any(word in text for word in search_words):
        return "search"

    # ---------------- Calculator ----------------

    calculator_words = [
        "sqrt(",
        "pow(",
        "round(",
        "+",
        "-",
        "*",
        "/"
    ]

    if any(word in text for word in calculator_words):
        return "calculator"

    return "gemini"