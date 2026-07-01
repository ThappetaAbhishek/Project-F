import requests

API_URL = "https://en.wikipedia.org/api/rest_v1/page/summary/"


def get_summary(query):
    """
    Returns a summary from the official Wikipedia API.
    """

    try:
        title = query.strip().replace(" ", "_")

        response = requests.get(
            API_URL + title,
            headers={
                "User-Agent": "Project-F"
            },
            timeout=10
        )

        if response.status_code == 404:
            return {
                "error": "Page not found."
            }

        if response.status_code != 200:
            return {
                "error": f"HTTP {response.status_code}"
            }

        data = response.json()

        return {
            "title": data.get("title", ""),
            "summary": data.get("extract", ""),
            "url": data.get("content_urls", {})
                      .get("desktop", {})
                      .get("page", "")
        }

    except Exception as e:
        return {
            "error": str(e)
        }