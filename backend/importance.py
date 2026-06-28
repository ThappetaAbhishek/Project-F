"""
importance.py

Determines whether a sentence should be stored
and assigns a category and importance score.
"""

IMPORTANT_PATTERNS = {

    # Highest priority first

    "goals": [
        "i'm learning",
        "i am learning",
        "i'm preparing",
        "i am preparing",
        "my goal is",
        "i want to become",
        "i'm building",
        "i am building"
    ],

    "preferences": [
        "i like",
        "i love",
        "i prefer",
        "my favorite",
        "my favourite"
    ],

    "profession": [
        "i work as",
        "my profession is"
    ],

    "profile": [
        "my name is",
        "call me",
        "my age is",
        "i live in",
        "my college is",
        "i study at",
        "my department is"
    ]
}


IMPORTANCE_SCORE = {
    "profile": 5,
    "goals": 4,
    "preferences": 3,
    "profession": 3
}


def analyze_importance(sentence):

    text = sentence.lower().strip()

    for category, phrases in IMPORTANT_PATTERNS.items():

        for phrase in phrases:

            if text.startswith(phrase):

                return {
                    "remember": True,
                    "category": category,
                    "importance": IMPORTANCE_SCORE[category]
                }

    return {
        "remember": False,
        "category": None,
        "importance": 0
    }