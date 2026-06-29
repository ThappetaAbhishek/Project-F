from backend.memory_manager import remember_preference


PREFERENCE_PHRASES = [
    "i like",
    "i love",
    "i prefer",
    "my favorite",
    "my favourite"
]


def can_handle(message):

    text = message.lower().strip()

    return any(
        text.startswith(phrase)
        for phrase in PREFERENCE_PHRASES
    )


def handle(message):

    text = message.lower().strip()

    if text.startswith("i like"):

        value = message[6:].strip()

        remember_preference("likes", value)

        return f"I'll remember that you like {value}."

    if text.startswith("i love"):

        value = message[6:].strip()

        remember_preference("likes", value)

        return f"I'll remember that you love {value}."

    if text.startswith("i prefer"):

        value = message[8:].strip()

        remember_preference("preference", value)

        return f"I'll remember that you prefer {value}."

    if text.startswith("my favorite") or text.startswith("my favourite"):

        value = message.split("is")[-1].strip()

        remember_preference("favorite", value)

        return f"I'll remember your favorite is {value}."

    return None