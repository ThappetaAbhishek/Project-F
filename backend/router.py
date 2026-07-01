from backend.agent import agent_answer

from backend.handlers.developer_handler import handle as developer_handle
from backend.handlers.profile_handler import handle as profile_handle
from backend.handlers.preference_handler import handle as preference_handle
from backend.handlers.goal_handler import handle as goal_handle
from backend.handlers.recall_handler import handle as recall_handle
from backend.handlers.gemini_handler import handle as gemini_handle


def route(message):
    """
    Main router for Project F.
    """

    text = message.lower().strip()

    # ---------------- Developer Commands ----------------

    if text.startswith("/"):
        return developer_handle(message)

    # ---------------- Profile ----------------

    if text.startswith("my name is") or text.startswith("call me"):
        return profile_handle(message)

    # ---------------- Preferences ----------------

    if (
        text.startswith("i like")
        or text.startswith("i love")
        or text.startswith("i enjoy")
        or text.startswith("i prefer")
    ):
        return preference_handle(message)

    # ---------------- Goals ----------------

    if (
        text.startswith("i'm learning")
        or text.startswith("i am learning")
        or text.startswith("i'm building")
        or text.startswith("i am building")
        or text.startswith("my goal is")
    ):
        return goal_handle(message)

    # ---------------- Recall ----------------

    if (
        "what is my name" in text
        or "my preferences" in text
        or "my goals" in text
    ):
        return recall_handle(message)

    # ---------------- AI Agent ----------------

    answer = agent_answer(message)

    if answer:
        return answer

    # ---------------- Gemini ----------------

    return gemini_handle(message)