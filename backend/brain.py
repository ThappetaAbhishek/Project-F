import os
from dotenv import load_dotenv
from google import genai

from memory.memory import (
    recall_fact,
    remember_sentence
)

from backend.prompt_builder import build_prompt
from backend.conversation import get_recent_conversation

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def get_response(message):
    message_lower = message.lower().strip()

    # ---------------- Remember Information ----------------

    memory_phrases = [
        "my name is",
        "call me",
        "my age is",
        "i live in",
        "my college is",
        "i study at",
        "my department is",
        "my favorite language is",
        "my favourite language is",
        "my favorite color is",
        "my favourite color is",
        "my hobby is",
        "my hobbies are",
        "i work as",
        "my profession is"
    ]

    if any(phrase in message_lower for phrase in memory_phrases):

        remember_sentence(message)

        if "my name is" in message_lower or "call me" in message_lower:
            name = recall_fact("name")
            if name:
                return f"Nice to meet you, {name}! I'll remember your name."

        return "Got it! I'll remember that."

    # ---------------- Recall Information ----------------

    recall_questions = {
        "what is my name": ("name", "Your name is"),
        "who am i": ("name", "Your name is"),

        "what is my age": ("age", "Your age is"),
        "how old am i": ("age", "Your age is"),

        "where do i live": ("city", "You live in"),
        "what is my city": ("city", "You live in"),

        "what is my college": ("college", "Your college is"),
        "where do i study": ("college", "Your college is"),

        "what is my department": ("department", "Your department is"),

        "what is my favorite language": ("favorite_language", "Your favorite language is"),
        "what is my favourite language": ("favorite_language", "Your favorite language is"),

        "what is my favorite color": ("favorite_color", "Your favorite color is"),
        "what is my favourite color": ("favorite_color", "Your favorite color is"),

        "what is my hobby": ("hobby", "Your hobby is"),

        "what is my profession": ("profession", "Your profession is"),
        "what do i do": ("profession", "Your profession is")
    }

    for question, (key, label) in recall_questions.items():
        if question in message_lower:
            value = recall_fact(key)

            if value:
                return f"{label} {value}."

            return "I don't know that yet."

    # ---------------- Conversation History ----------------

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