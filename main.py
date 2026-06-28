from backend.brain import get_response
from memory.memory import remember


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

        response = get_response(user)

        remember(user, response)

        print("Project F:", response)


if __name__ == "__main__":
    main()