"""
Intent definitions for Project F.

Every tool declares the words that indicate
it can answer a user's request.
"""

INTENTS = {

    "weather": [
        "weather",
        "temperature",
        "forecast",
        "humidity",
        "wind"
    ],

    "news": [
        "news",
        "latest",
        "headline",
        "breaking"
    ],

    "wiki": [
        "who is",
        "what is",
        "tell me about",
        "define",
        "explain"
    ],

    "search": [
        "/search",
        "search",
        "find",
        "look up"
    ],

    "calculator": [
        "sqrt(",
        "pow(",
        "round(",
        "+",
        "-",
        "*",
        "/"
    ]
}