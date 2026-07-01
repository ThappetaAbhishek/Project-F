from backend.multi_decision_engine import decide_all
from backend.tool_executor import execute
from backend.ai_summarizer import summarize


def agent_answer(message):
    """
    Executes multiple tools and summarizes the results.
    """

    intents = decide_all(message)

    if not intents:
        return None

    tool_output = execute(intents, message)

    if not tool_output.strip():
        return None

    return summarize(message, tool_output)