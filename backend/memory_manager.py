from memory.memory import (
    load_user_memory,
    save_user_memory
)


def remember_preference(key, value):
    """
    Stores user preferences like:
    favorite language,
    favorite color,
    hobby,
    etc.
    """

    memory = load_user_memory()

    if "preferences" not in memory:
        memory["preferences"] = {}

    memory["preferences"][key] = value

    save_user_memory(memory)


def remember_goal(goal):
    """
    Stores long-term user goals.
    Example:
    - Learning Java
    - Preparing for interviews
    - Building Project F
    """

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