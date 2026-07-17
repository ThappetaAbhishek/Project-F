from backend.memory_service import (
    save_profile,
    get_profile
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

    text = message.strip()

    lower = text.lower()

    # ---------------- Name ----------------

    if lower.startswith("my name is"):

        name = text[11:].strip()

        save_profile("name", name)

        return f"Nice to meet you, {name}! I'll remember your name."

    if lower.startswith("call me"):

        name = text[7:].strip()

        save_profile("name", name)

        return f"Sure! I'll call you {name}."

    # ---------------- Age ----------------

    if lower.startswith("my age is"):

        age = text[9:].strip()

        save_profile("age", age)

        return "Got it! I'll remember your age."

    # ---------------- City ----------------

    if lower.startswith("i live in"):

        city = text[9:].strip()

        save_profile("city", city)

        return f"Nice! I'll remember that you live in {city}."

    # ---------------- College ----------------

    if lower.startswith("my college is"):

        college = text[14:].strip()

        save_profile("college", college)

        return "I'll remember your college."

    if lower.startswith("i study at"):

        college = text[10:].strip()

        save_profile("college", college)

        return "I'll remember where you study."

    # ---------------- Department ----------------

    if lower.startswith("my department is"):

        department = text[17:].strip()

        save_profile("department", department)

        return "I'll remember your department."

    return "Got it! I'll remember that."