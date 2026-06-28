import json
import os

CHAT_MEMORY_FILE = "memory/chat_memory.json"
USER_MEMORY_FILE = "memory/user_memory.json"


# ---------------- Chat History ----------------

def load_memory():
    if not os.path.exists(CHAT_MEMORY_FILE):
        return []

    with open(CHAT_MEMORY_FILE, "r") as file:
        return json.load(file)


def save_memory(memory):
    with open(CHAT_MEMORY_FILE, "w") as file:
        json.dump(memory, file, indent=4)


def remember(user, bot):
    memory = load_memory()

    memory.append({
        "user": user,
        "bot": bot
    })

    save_memory(memory)


# ---------------- User Memory ----------------

def load_user_memory():
    if not os.path.exists(USER_MEMORY_FILE):
        return {}

    with open(USER_MEMORY_FILE, "r") as file:
        return json.load(file)


def save_user_memory(memory):
    with open(USER_MEMORY_FILE, "w") as file:
        json.dump(memory, file, indent=4)


def remember_fact(key, value):
    memory = load_user_memory()
    memory[key] = value
    save_user_memory(memory)


def recall_fact(key):
    memory = load_user_memory()
    return memory.get(key)


# ---------------- Natural Memory ----------------

def remember_sentence(sentence):
    memory = load_user_memory()

    text = sentence.lower().strip()

    facts = {
        "my name is": "name",
        "call me": "name",

        "my age is": "age",

        "i live in": "city",

        "my college is": "college",
        "i study at": "college",

        "my department is": "department",

        "my favorite language is": "favorite_language",
        "my favourite language is": "favorite_language",

        "my favorite color is": "favorite_color",
        "my favourite color is": "favorite_color",

        "my hobby is": "hobby",
        "my hobbies are": "hobby",

        "i work as": "profession",
        "my profession is": "profession"
    }

    for phrase, key in facts.items():

        if text.startswith(phrase):

            value = sentence[len(phrase):].strip()

            if value:
                memory[key] = value

            save_user_memory(memory)
            return