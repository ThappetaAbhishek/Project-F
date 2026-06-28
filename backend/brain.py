import os
from dotenv import load_dotenv
from google import genai

from memory.memory import (
    recall_fact,
    remember_sentence
)

from backend.memory_manager import (
    remember_goal,
    remember_preference,
    get_goals,
    get_preferences
)

from backend.prompt_builder import build_prompt
from backend.conversation import get_recent_conversation

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def get_response(message):

    message_lower = message.lower().strip()

    # ---------------- Save Preferences ----------------

    if message_lower.startswith("i like "):
        value = message[7:].strip()
        remember_preference("likes", value)
        return f"I'll remember that you like {value}."

    if message_lower.startswith("i love "):
        value = message[7:].strip()
        remember_preference("loves", value)
        return f"I'll remember that you love {value}."

    if message_lower.startswith("i prefer "):
        value = message[9:].strip()
        remember_preference("preference", value)
        return f"I'll remember that you prefer {value}."

    # ---------------- Save Goals ----------------

    if message_lower.startswith("i am learning "):
        goal = "Learning " + message[14:].strip()
        remember_goal(goal)
        return f"Awesome! I'll remember that you're {goal.lower()}."

    if message_lower.startswith("i'm learning "):
        goal = "Learning " + message[13:].strip()
        remember_goal(goal)
        return f"Awesome! I'll remember that you're {goal.lower()}."

    if message_lower.startswith("i am preparing for "):
        goal = "Preparing for " + message[20:].strip()
        remember_goal(goal)
        return f"Great! I'll remember that you're {goal.lower()}."

    if message_lower.startswith("i'm preparing for "):
        goal = "Preparing for " + message[19:].strip()
        remember_goal(goal)
        return f"Great! I'll remember that you're {goal.lower()}."

    if message_lower.startswith("i am building "):
        goal = "Building " + message[14:].strip()
        remember_goal(goal)
        return f"Nice! I'll remember that you're {goal.lower()}."

    if message_lower.startswith("i'm building "):
        goal = "Building " + message[13:].strip()
        remember_goal(goal)
        return f"Nice! I'll remember that you're {goal.lower()}."

    # ---------------- Existing Memory ----------------

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

    # ---------------- Recall Personal Facts ----------------

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
        "what is my profession": ("profession", "Your profession is")
    }

    for question, (key, label) in recall_questions.items():

        if question in message_lower:

            value = recall_fact(key)

            if value:
                return f"{label} {value}."

            return "I don't know that yet."

    # ---------------- Recall Goals ----------------

    if "what are my goals" in message_lower:

        goals = get_goals()

        if goals:
            return "Your goals are:\n• " + "\n• ".join(goals)

        return "I don't know your goals yet."

    # ---------------- Recall Preferences ----------------

    if "what do i like" in message_lower:

        preferences = get_preferences()

        if preferences:

            text = []

            for key, value in preferences.items():
                text.append(f"{key}: {value}")

            return "\n".join(text)

        return "I don't know your preferences yet."

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