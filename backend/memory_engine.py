import json
import os

MEMORY_FILE = "memory/memory_v2.json"


def load_memory():

    if not os.path.exists(MEMORY_FILE):

        return {
            "profile": {},
            "preferences": {},
            "goals": [],
            "projects": [],
            "facts": [],
            "skills": [],
            "conversations": []
        }

    with open(MEMORY_FILE, "r", encoding="utf-8") as f:

        return json.load(f)


def save_memory(memory):

    with open(MEMORY_FILE, "w", encoding="utf-8") as f:

        json.dump(memory, f, indent=4)


def add(category, value):

    memory = load_memory()

    if isinstance(memory[category], list):

        if value not in memory[category]:
            memory[category].append(value)

    elif isinstance(memory[category], dict):

        memory[category].update(value)

    save_memory(memory)


def get(category):

    return load_memory()[category]