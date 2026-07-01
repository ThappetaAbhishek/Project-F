"""
Project F Tool Executor

Executes multiple tools and combines their responses.
"""

from backend.handlers.weather_handler import handle as weather_handle
from backend.handlers.news_handler import handle as news_handle
from backend.handlers.wiki_handler import handle as wiki_handle
from backend.handlers.search_handler import handle as search_handle
from backend.handlers.calculator_handler import handle as calculator_handle


TOOLS = {
    "weather": weather_handle,
    "news": news_handle,
    "wiki": wiki_handle,
    "search": search_handle,
    "calculator": calculator_handle
}


def execute(intents, message):

    responses = []

    for intent in intents:

        handler = TOOLS.get(intent)

        if handler is None:
            continue

        try:

            result = handler(message)

            if result:
                responses.append(result)

        except Exception as e:

            responses.append(
                f"{intent} failed: {e}"
            )

    return "\n\n" + ("\n" + "=" * 70 + "\n\n").join(responses)