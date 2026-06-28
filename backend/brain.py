import os
from dotenv import load_dotenv
from google import genai

from backend.prompt_builder import build_prompt
from backend.conversation import get_recent_conversation

from backend.importance import analyze_importance
from backend.memory_manager import process_memory

from backend.handlers.profile_handler import (
    can_handle as profile_can_handle,
    handle as profile_handle
)

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def get_response(message):

    # ---------------- Profile Handler ----------------

    if profile_can_handle(message):
        return profile_handle(message)

    # ---------------- Intelligent Memory ----------------

    analysis = analyze_importance(message)

    if analysis["remember"]:

        process_memory(
            message,
            analysis["category"],
            analysis["importance"]
        )

        return (
            "I'll remember that.\n"
            f"(Category: {analysis['category']}, "
            f"Importance: {analysis['importance']})"
        )

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