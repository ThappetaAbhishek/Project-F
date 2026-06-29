from memory.memory import recall_fact
from backend.memory_manager import (
    get_preferences,
    get_goals
)


RECALL_QUESTIONS = {

    "what is my name": "name",
    "who am i": "name",

    "what is my age": "age",
    "how old am i": "age",

    "where do i live": "city",

    "what is my college": "college",

    "what is my department": "department",

    "what do i like": "preferences",

    "what are my goals": "goals"
}


def can_handle(message):

    text = message.lower().strip()

    return text in RECALL_QUESTIONS


def handle(message):

    text = message.lower().strip()

    question = RECALL_QUESTIONS[text]

    # ---------------- Profile ----------------

    if question in [
        "name",
        "age",
        "city",
        "college",
        "department"
    ]:

        value = recall_fact(question)

        if value:

            labels = {
                "name": "Your name is",
                "age": "Your age is",
                "city": "You live in",
                "college": "Your college is",
                "department": "Your department is"
            }

            return f"{labels[question]} {value}."

        return "I don't know that yet."

    # ---------------- Preferences ----------------

    if question == "preferences":

        prefs = get_preferences()

        if not prefs:
            return "I don't know your preferences yet."

        lines = []

        for key, value in prefs.items():
            lines.append(f"{key}: {value}")

        return "\n".join(lines)

    # ---------------- Goals ----------------

    if question == "goals":

        goals = get_goals()

        if not goals:
            return "I don't know your goals yet."

        result = "Your goals are:\n\n"

        for goal in goals:
            result += f"• {goal}\n"

        return result