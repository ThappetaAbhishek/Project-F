from memory.memory import load_memory


def get_recent_conversation(limit=6):
    """
    Returns the last few conversations in a readable format
    for the AI prompt.
    """

    history = load_memory()

    if not history:
        return "No previous conversation."

    recent = history[-limit:]

    conversation = []

    for chat in recent:
        conversation.append(f"User: {chat['user']}")
        conversation.append(f"Project F: {chat['bot']}")

    return "\n".join(conversation)