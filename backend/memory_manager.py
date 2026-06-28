from memory.memory import (
    load_user_memory,
    save_user_memory,
    remember_sentence
)


def remember_preference(key, value):

    memory = load_user_memory()

    if "preferences" not in memory:
        memory["preferences"] = {}

    memory["preferences"][key] = value

    save_user_memory(memory)


def remember_goal(goal):

    memory = load_user_memory()

    if "goals" not in memory:
        memory["goals"] = []

    if goal not in memory["goals"]:
        memory["goals"].append(goal)

    save_user_memory(memory)


def get_preferences():

    memory = load_user_memory()

    return memory.get("preferences", {})


def get_goals():

    memory = load_user_memory()

    return memory.get("goals", [])


# --------------------------------------------------
# NEW FUNCTION
# --------------------------------------------------

def process_memory(sentence, category, importance):
    """
    Stores information according to its category.
    """

    text = sentence.lower().strip()

    # Profile information
    if category == "profile":
        remember_sentence(sentence)
        return

    # Preferences
    if category == "preferences":

        if text.startswith("i like"):
            remember_preference(
                "likes",
                sentence[6:].strip()
            )

        elif text.startswith("i love"):
            remember_preference(
                "likes",
                sentence[6:].strip()
            )

        elif text.startswith("i prefer"):
            remember_preference(
                "preference",
                sentence[8:].strip()
            )

        elif text.startswith("my favorite"):
            remember_preference(
                "favorite",
                sentence.replace("My favorite", "").strip()
            )

        return

    # Goals
    if category == "goals":

        if text.startswith("i'm"):
            remember_goal(sentence[4:].strip())

        elif text.startswith("i am"):
            remember_goal(sentence[5:].strip())

        elif text.startswith("my goal is"):
            remember_goal(sentence[10:].strip())

        elif text.startswith("i want to become"):
            remember_goal(sentence[16:].strip())

        return