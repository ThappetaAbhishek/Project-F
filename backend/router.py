from backend.handlers.developer_handler import (
    can_handle as developer_can_handle,
    handle as developer_handle
)

from backend.handlers.calculator_handler import (
    can_handle as calculator_can_handle,
    handle as calculator_handle
)

from backend.handlers.weather_handler import (
    can_handle as weather_can_handle,
    handle as weather_handle
)

from backend.handlers.news_handler import (
    can_handle as news_can_handle,
    handle as news_handle
)

from backend.handlers.search_handler import (
    can_handle as search_can_handle,
    handle as search_handle
)

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


HANDLERS = [

    (developer_can_handle, developer_handle),

    (calculator_can_handle, calculator_handle),

    (weather_can_handle, weather_handle),

    (news_can_handle, news_handle),

    (search_can_handle, search_handle),

    (profile_can_handle, profile_handle),

    (preference_can_handle, preference_handle),

    (goal_can_handle, goal_handle),

    (recall_can_handle, recall_handle),
]


def route(message):
    """
    Routes the user message to the appropriate handler.
    """

    for can_handle, handle in HANDLERS:

        if can_handle(message):
            return handle(message)

    return gemini_handle(message)