import os
from dotenv import load_dotenv
from google import genai

from memory.memory import remember_fact, recall_fact

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def get_response(message):
    message_lower = message.lower()

    # ---------- Remember user's name ----------
    if "my name is" in message_lower:
        name = message[message_lower.find("my name is") + len("my name is"):].strip().title()
        remember_fact("name", name)
        return f"Nice to meet you, {name}! I'll remember your name."

    # ---------- Recall user's name ----------
    if "what is my name" in message_lower:
        name = recall_fact("name")
        if name:
            return f"Your name is {name}."
        else:
            return "I don't know your name yet."

    # ---------- AI Prompt ----------
    prompt = f"""
You are Project F, a friendly AI assistant.

Rules:
- Your name is Project F.
- Never say you are Gemini or Google.
- Never say you are a large language model.
- Always introduce yourself as Project F.
- Answer naturally and helpfully.

User: {message}
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text.strip()

    except Exception as e:
        return f"Error: {e}"