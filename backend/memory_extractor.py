import re

from backend.memory_service import (
    save_project,
    save_skill,
    save_goal
)


SKILLS = [
    "python",
    "java",
    "c",
    "c++",
    "javascript",
    "typescript",
    "react",
    "flask",
    "django",
    "fastapi",
    "node",
    "node.js",
    "express",
    "mysql",
    "sqlite",
    "mongodb",
    "git",
    "docker",
    "aws"
]


def clean_project_name(project):

    separators = [
        " using ",
        " with ",
        " in ",
        " built",
        " on "
    ]

    project = project.strip()

    for sep in separators:

        if sep.lower() in project.lower():

            project = project.split(sep, 1)[0]

    return project.strip(" .,")


def normalize_goal(goal):

    goal = goal.strip()

    goal = re.sub(
        r"^i want to\s+",
        "",
        goal,
        flags=re.IGNORECASE
    )

    goal = re.sub(
        r"^my goal is\s+",
        "",
        goal,
        flags=re.IGNORECASE
    )

    return goal.strip().capitalize()


def extract(message):

    text = message.lower()

    # ---------------- Projects ----------------

    match = re.search(
        r"(?:building|working on|developing)\s+(.*)",
        message,
        re.IGNORECASE
    )

    if match:

        project = clean_project_name(
            match.group(1)
        )

        if project:

            save_project(project)

    # ---------------- Goals ----------------

    if "i want to" in text:

        save_goal(
            normalize_goal(message)
        )

    elif "my goal is" in text:

        save_goal(
            normalize_goal(message)
        )

    # ---------------- Skills ----------------

    words = re.findall(r"[A-Za-z0-9.+#]+", text)

    for skill in SKILLS:

        if skill == "c":

            if "c" in words:

                save_skill("C")

            continue

        if skill in text:

            save_skill(skill.title())