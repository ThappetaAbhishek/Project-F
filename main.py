from backend.brain import get_response
from backend.memory_extractor import extract
from backend.ai_memory_extractor import extract_memory
from backend.memory_service import (
    save_project,
    save_skill,
    save_goal,
    save_fact
)

from memory.memory import remember


def save_ai_memory(data):
    """
    Save AI-extracted memories into SQLite.
    """

    for project in data.get("projects", []):
        save_project(project)

    for skill in data.get("skills", []):
        save_skill(skill)

    for goal in data.get("goals", []):
        save_goal(goal)

    for fact in data.get("facts", []):
        save_fact(fact)


def main():

    print("=" * 30)
    print("PROJECT F")
    print("=" * 30)
    print("Hello! I am Project F.")
    print("Type 'exit' to quit.\n")

    while True:

        user = input("You: ")

        if user.lower() == "exit":
            print("Project F: Goodbye!")
            break

        # -------------------------
        # Existing Regex Extractor
        # -------------------------

        extract(user)

        # -------------------------
        # AI Memory Extractor
        # -------------------------

        memory = extract_memory(user)

        save_ai_memory(memory)

        # -------------------------
        # AI Response
        # -------------------------

        response = get_response(user)

        # -------------------------
        # Chat Memory
        # -------------------------

        remember(user, response)

        print("Project F:", response)


if __name__ == "__main__":
    main()