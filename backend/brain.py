import os
from dotenv import load_dotenv
from google import genai

from backend.prompt_builder import build_prompt
from backend.conversation import get_recent_conversation

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

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def get_response(message):

    # ---------------- Profile ----------------

    if profile_can_handle(message):
        return profile_handle(message)

    # ---------------- Preferences ----------------

    if preference_can_handle(message):
        return preference_handle(message)

    # ---------------- Goals ----------------

    if goal_can_handle(message):
        return goal_handle(message)

    # ---------------- Conversation ----------------

    conversation = get_recent_conversation()

    # ---------------- Prompt ----------------

    prompt = build_prompt(
        user_message=message,
        conversation_history=conversation
    )

    # ---------------- Gemini ----------------

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text.strip()

    except Exception as e:

        return f"Error: {e}"