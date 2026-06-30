from tools.news import get_news


def can_handle(message):
    """
    Detect news-related queries.
    """

    text = message.lower()

    keywords = [
        "news",
        "latest",
        "headlines",
        "breaking"
    ]

    return any(word in text for word in keywords)


def handle(message):

    original = message.strip()
    lower = original.lower()

    prefixes = [
        "latest news about",
        "latest news on",
        "latest news",
        "news about",
        "news on",
        "breaking news about",
        "breaking news on",
        "breaking news",
        "latest",
        "news"
    ]

    topic = original

    for prefix in prefixes:
        if lower.startswith(prefix):
            topic = original[len(prefix):].strip()
            break

    if not topic:
        topic = "technology"

    articles = get_news(topic)

    if not articles:
        return "No news found."

    if "error" in articles[0]:
        return f"News Error: {articles[0]['error']}"

    response = []

    for i, article in enumerate(articles, start=1):

        response.append(
            f"""{i}. {article['title']}

{article['link']}
"""
        )

    return "\n".join(response)