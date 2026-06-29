from memory.memory import load_user_memory, load_memory


COMMANDS = [
    "/help",
    "/memory",
    "/profile",
    "/preferences",
    "/goals",
    "/stats",
    "/version"
]


def can_handle(message):

    return message.lower().strip() in COMMANDS


def handle(message):

    command = message.lower().strip()

    user_memory = load_user_memory()
    chat_memory = load_memory()

    # ---------------- HELP ----------------

    if command == "/help":

        return """
Developer Commands

/help
/profile
/preferences
/goals
/memory
/stats
/version
""".strip()

    # ---------------- PROFILE ----------------

    if command == "/profile":

        text = []

        for key in [
            "name",
            "age",
            "city",
            "college",
            "department"
        ]:

            if key in user_memory:
                text.append(f"{key}: {user_memory[key]}")

        return "\n".join(text) if text else "No profile stored."

    # ---------------- PREFERENCES ----------------

    if command == "/preferences":

        prefs = user_memory.get("preferences", {})

        if not prefs:
            return "No preferences stored."

        result = []

        for key, value in prefs.items():
            result.append(f"{key}: {value}")

        return "\n".join(result)

    # ---------------- GOALS ----------------

    if command == "/goals":

        goals = user_memory.get("goals", [])

        if not goals:
            return "No goals stored."

        result = []

        for goal in goals:
            result.append(f"• {goal}")

        return "\n".join(result)

    # ---------------- MEMORY ----------------

    if command == "/memory":

        return str(user_memory)

    # ---------------- STATS ----------------

    if command == "/stats":

        profile = 0

        for key in [
            "name",
            "age",
            "city",
            "college",
            "department"
        ]:

            if key in user_memory:
                profile += 1

        preferences = len(user_memory.get("preferences", {}))
        goals = len(user_memory.get("goals", []))
        chats = len(chat_memory)

        return f"""
Project F Statistics

Profile Facts : {profile}

Preferences : {preferences}

Goals : {goals}

Conversations : {chats}

Version : 1.7.1
""".strip()

    # ---------------- VERSION ----------------

    if command == "/version":

        return "Project F Version 1.7.1"

    return None