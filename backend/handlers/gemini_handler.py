from google import genai

from backend.config import (
    GEMINI_API_KEY,
    GEMINI_MODEL
)

from backend.prompt_builder import build_prompt
from backend.conversation import get_recent_conversation
from backend.logger import logger


client = genai.Client(
    api_key=GEMINI_API_KEY
)


def handle(message):
    """
    Handles all requests that reach Gemini.
    """

    conversation = get_recent_conversation()

    prompt = build_prompt(
        user_message=message,
        conversation_history=conversation
    )

    try:
        logger.info(f"Gemini Request: {message}")

        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt
        )

        answer = response.text.strip()

        logger.info("Gemini Response Generated Successfully")

        return answer

    except Exception as e:
        logger.error(f"Gemini Error: {e}")

        return f"Gemini Error: {e}"