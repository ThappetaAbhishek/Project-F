import json
import os

MEMORY_FILE = "memory/chat_memory.json"


def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return []

    with open(MEMORY_FILE, "r") as file:
        return json.load(file)


def save_memory(memory):
    with open(MEMORY_FILE, "w") as file:
        json.dump(memory, file, indent=4)


def remember(user, bot):
    memory = load_memory()

    memory.append({
        "user": user,
        "bot": bot
    })

    save_memory(memory)
    
    save_memory(memory)


USER_MEMORY_FILE = "memory/user_memory.json"


def load_user_memory():
    if not os.path.exists(USER_MEMORY_FILE):
        return {}

    with open(USER_MEMORY_FILE, "r") as file:
        return json.load(file)


def save_user_memory(data):
    with open(USER_MEMORY_FILE, "w") as file:
        json.dump(data, file, indent=4)


def remember_fact(key, value):
    memory = load_user_memory()
    memory[key] = value
    save_user_memory(memory)


def recall_fact(key):
    memory = load_user_memory()
    return memory.get(key)

def remember_sentence(sentence):
    memory = load_user_memory()

    sentence = sentence.lower()

    if "my age is" in sentence:
        memory["age"] = sentence.replace("my age is", "").strip()

    elif "i live in" in sentence:
        memory["city"] = sentence.replace("i live in", "").strip()

    elif "my favorite language is" in sentence:
        memory["favorite_language"] = sentence.replace(
            "my favorite language is", ""
        ).strip()

    elif "my college is" in sentence:
        memory["college"] = sentence.replace("my college is", "").strip()

    elif "my department is" in sentence:
        memory["department"] = sentence.replace("my department is", "").strip()

    save_user_memory(memory)