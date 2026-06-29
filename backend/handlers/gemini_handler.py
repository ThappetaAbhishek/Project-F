import os

from dotenv import load_dotenv
from google import genai

from backend.prompt_builder import build_prompt
from backend.conversation import get_recent_conversation

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def handle(message):

    conversation = get_recent_conversation()

    prompt = build_prompt(
        user_message=message,
        conversation_history=conversation
    )

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text.strip()

    except Exception as e:

        return f"Error: {e}"