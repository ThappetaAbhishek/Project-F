"""
Project F Multi Decision Engine

Returns all matching intents instead of just one.
"""

from backend.intents import INTENTS


def decide_all(message):

    text = message.lower().strip()

    matches = []

    for intent, keywords in INTENTS.items():

        score = 0

        for keyword in keywords:

            if keyword.startswith("/"):
                if text.startswith(keyword):
                    score += 5

            elif " " in keyword:
                if text.startswith(keyword):
                    score += 4

            else:
                if keyword in text:
                    score += 2

        if score > 0:
            matches.append((intent, score))

    matches.sort(key=lambda x: x[1], reverse=True)

    return [intent for intent, score in matches]