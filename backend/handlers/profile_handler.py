from memory.memory import (
    remember_sentence,
    recall_fact
)


PROFILE_PHRASES = [
    "my name is",
    "call me",
    "my age is",
    "i live in",
    "my college is",
    "i study at",
    "my department is"
]


def can_handle(message):

    text = message.lower().strip()

    return any(
        text.startswith(phrase)
        for phrase in PROFILE_PHRASES
    )


def handle(message):

    remember_sentence(message)

    text = message.lower().strip()

    if text.startswith("my name is") or text.startswith("call me"):

        name = recall_fact("name")

        if name:

            return (
                f"Nice to meet you, {name}!\n"
                "I'll remember your name."
            )

    return "Got it! I'll remember that."