from tools.search import search
from backend.semantic import SEARCH_PATTERNS


def can_handle(message):
    """
    Detects whether the user's message is asking
    for an internet search.
    """

    text = message.lower().strip()

    for pattern in SEARCH_PATTERNS:
        if text.startswith(pattern):
            return True

    return False


def handle(message):
    """
    Handles all search requests.

    Supported examples:

    /search Python
    Search Python
    Search for Spring Boot
    Find Java tutorials
    Look up Django
    Tell me about Python
    Who is Elon Musk?
    Latest AI news
    """

    query = message.strip()

    prefixes = [
        "/search",
        "search for",
        "search the web for",
        "search the web",
        "search internet for",
        "search internet",
        "search",
        "find information about",
        "find information",
        "find",
        "look up information",
        "look up",
        "tell me about",
        "who is",
        "what is",
        "where is",
        "when was",
        "latest",
        "news about"
    ]

    lower = query.lower()

    for prefix in prefixes:
        if lower.startswith(prefix):
            query = query[len(prefix):].strip()
            break

    if not query:
        return "What would you like me to search for?"

    results = search(query)

    if not results:
        return f"No search results found for '{query}'."

    response = []

    for i, item in enumerate(results, start=1):

        title = item.get("title", "")
        body = item.get("body", "")
        url = item.get("url", "")

        response.append(
            f"""{i}. {title}

{body}

{url}
"""
        )

    return "\n".join(response)