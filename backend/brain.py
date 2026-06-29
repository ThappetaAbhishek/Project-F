from backend.handlers.profile_handler import (
    can_handle as profile_can_handle,
    handle as profile_handle
)

from backend.handlers.preference_handler import (
    can_handle as preference_can_handle,
    handle as preference_handle
)

from backend.handlers.goal_handler import (
    can_handle as goal_can_handle,
    handle as goal_handle
)

from backend.handlers.recall_handler import (
    can_handle as recall_can_handle,
    handle as recall_handle
)

from backend.handlers.gemini_handler import (
    handle as gemini_handle
)


def get_response(message):

    # -------- Profile --------

    if profile_can_handle(message):
        return profile_handle(message)

    # -------- Preferences --------

    if preference_can_handle(message):
        return preference_handle(message)

    # -------- Goals --------

    if goal_can_handle(message):
        return goal_handle(message)

    # -------- Recall --------

    if recall_can_handle(message):
        return recall_handle(message)

    # -------- Gemini --------

    return gemini_handle(message)