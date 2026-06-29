from backend.memory_manager import (
    remember_preference,
    get_preferences
)

from backend.semantic import PREFERENCE_PATTERNS


def can_handle(message):

    text = message.lower().strip()

    for patterns in PREFERENCE_PATTERNS.values():

        for phrase in patterns:

            if text.startswith(phrase):
                return True

    return False


def handle(message):

    text = message.lower().strip()

    # ---------- Likes ----------

    for phrase in PREFERENCE_PATTERNS["likes"]:

        if text.startswith(phrase):

            value = message[len(phrase):].strip()

            remember_preference("likes", value)

            return f"I'll remember that you like {value}."

    # ---------- Favorite Color ----------

    for phrase in PREFERENCE_PATTERNS["favorite_color"]:

        if text.startswith(phrase):

            value = message[len(phrase):].strip()

            remember_preference("favorite_color", value)

            return f"I'll remember your favorite color is {value}."

    # ---------- Hobby ----------

    for phrase in PREFERENCE_PATTERNS["hobby"]:

        if text.startswith(phrase):

            value = message[len(phrase):].strip()

            remember_preference("hobby", value)

            return f"I'll remember your hobby is {value}."

    return None