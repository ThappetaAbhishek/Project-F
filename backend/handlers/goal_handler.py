from backend.memory_manager import remember_goal


GOAL_PHRASES = [
    "i'm learning",
    "i am learning",
    "i'm building",
    "i am building",
    "i'm preparing",
    "i am preparing",
    "my goal is",
    "i want to become"
]


def can_handle(message):

    text = message.lower().strip()

    return any(
        text.startswith(phrase)
        for phrase in GOAL_PHRASES
    )


def handle(message):

    text = message.lower().strip()

    if text.startswith("i'm learning"):
        goal = message[13:].strip()

    elif text.startswith("i am learning"):
        goal = message[14:].strip()

    elif text.startswith("i'm building"):
        goal = message[13:].strip()

    elif text.startswith("i am building"):
        goal = message[14:].strip()

    elif text.startswith("i'm preparing"):
        goal = message[14:].strip()

    elif text.startswith("i am preparing"):
        goal = message[15:].strip()

    elif text.startswith("my goal is"):
        goal = message[10:].strip()

    elif text.startswith("i want to become"):
        goal = message[16:].strip()

    else:
        return None

    remember_goal(goal)

    return f"I'll remember your goal: {goal}."