import feedparser


def get_news(topic="technology", max_results=5):
    """
    Fetch latest news from Google News RSS.
    No API key required.
    """

    try:
        url = (
            f"https://news.google.com/rss/search?"
            f"q={topic.replace(' ', '+')}&hl=en-IN&gl=IN&ceid=IN:en"
        )

        feed = feedparser.parse(url)

        news = []

        for entry in feed.entries[:max_results]:
            news.append({
                "title": entry.title,
                "summary": entry.summary,
                "link": entry.link
            })

        return news

    except Exception as e:
        return [{"error": str(e)}]