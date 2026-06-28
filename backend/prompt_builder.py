"""
Project F Prompt Builder

This module builds the prompt that is sent to Gemini.
Keeping it separate makes brain.py much cleaner.
"""

from memory.memory import load_memory


def build_prompt(user_message):
    """
    Builds the final prompt using:
    - Project F personality
    - Recent conversation history
    - Current user message
    """

    history = load_memory()

    recent_history = history[-10:]

    conversation = ""

    for chat in recent_history:
        conversation += f"User: {chat['user']}\n"
        conversation += f"Project F: {chat['bot']}\n\n"

    prompt = f"""
You are Project F, an intelligent AI assistant.

Rules:

- Your name is Project F.
- Never say you are Gemini.
- Never say you are Google AI.
- Never say you are a Large Language Model.
- Speak naturally.
- Be friendly.
- Be professional.
- Keep answers clear and helpful.
- Remember previous conversation if it is relevant.

Conversation History:

{conversation}

Current User Message:

User: {user_message}

Project F:
"""

    return prompt