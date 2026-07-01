from backend.decision_engine import decide

from backend.handlers.developer_handler import handle as developer_handle
from backend.handlers.calculator_handler import handle as calculator_handle
from backend.handlers.weather_handler import handle as weather_handle
from backend.handlers.news_handler import handle as news_handle
from backend.handlers.wiki_handler import handle as wiki_handle
from backend.handlers.search_handler import handle as search_handle
from backend.handlers.profile_handler import handle as profile_handle
from backend.handlers.preference_handler import handle as preference_handle
from backend.handlers.goal_handler import handle as goal_handle
from backend.handlers.recall_handler import handle as recall_handle
from backend.handlers.gemini_handler import handle as gemini_handle


def route(message):
    """
    Routes user requests using the Decision Engine.
    """

    intent = decide(message)

    if intent == "calculator":
        return calculator_handle(message)

    if intent == "weather":
        return weather_handle(message)

    if intent == "news":
        return news_handle(message)

    if intent == "wiki":
        return wiki_handle(message)

    if intent == "search":
        return search_handle(message)

    # Keep these handlers for memory-related features
    text = message.lower()

    if text.startswith("my name is") or text.startswith("call me"):
        return profile_handle(message)

    if (
        text.startswith("i like")
        or text.startswith("i love")
        or text.startswith("i enjoy")
        or text.startswith("i prefer")
    ):
        return preference_handle(message)

    if (
        text.startswith("i'm learning")
        or text.startswith("i am learning")
        or text.startswith("i'm building")
        or text.startswith("i am building")
        or text.startswith("my goal is")
    ):
        return goal_handle(message)

    if (
        "what is my name" in text
        or "my preferences" in text
        or "my goals" in text
    ):
        return recall_handle(message)

    if text.startswith("/"):
        return developer_handle(message)

    return gemini_handle(message)