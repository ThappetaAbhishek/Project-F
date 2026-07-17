from backend.memory_service import (
    get_profile,
    get_preference,
    get_goals,
    get_projects,
    get_skills
)


RECALL_QUESTIONS = {

    "what is my name": "name",
    "who am i": "name",

    "what is my age": "age",
    "how old am i": "age",

    "where do i live": "city",

    "what is my college": "college",

    "what is my department": "department",

    "what do i like": "likes",

    "what is my favorite color": "favorite_color",

    "what is my hobby": "hobby",

    "what are my goals": "goals",

    "what are my projects": "projects",

    "what are my skills": "skills"
}


def can_handle(message):

    text = message.lower().strip()

    return text in RECALL_QUESTIONS


def handle(message):

    text = message.lower().strip()

    question = RECALL_QUESTIONS[text]

    # ---------------- Profile ----------------

    if question in [
        "name",
        "age",
        "city",
        "college",
        "department"
    ]:

        value = get_profile(question)

        if value:

            labels = {
                "name": "Your name is",
                "age": "Your age is",
                "city": "You live in",
                "college": "Your college is",
                "department": "Your department is"
            }

            return f"{labels[question]} {value}."

        return "I don't know that yet."

    # ---------------- Preferences ----------------

    if question in [
        "likes",
        "favorite_color",
        "hobby"
    ]:

        value = get_preference(question)

        if value:

            labels = {
                "likes": "You like",
                "favorite_color": "Your favorite color is",
                "hobby": "Your hobby is"
            }

            return f"{labels[question]} {value}."

        return "I don't know that yet."

    # ---------------- Goals ----------------

    if question == "goals":

        goals = get_goals()

        if not goals:
            return "I don't know your goals yet."

        result = "Your goals are:\n\n"

        for goal in goals:
            result += f"• {goal}\n"

        return result

    # ---------------- Projects ----------------

    if question == "projects":

        projects = get_projects()

        if not projects:
            return "I don't know your projects yet."

        result = "Your projects are:\n\n"

        for project in projects:
            result += f"• {project}\n"

        return result

    # ---------------- Skills ----------------

    if question == "skills":

        skills = get_skills()

        if not skills:
            return "I don't know your skills yet."

        result = "Your skills are:\n\n"

        for skill in skills:
            result += f"• {skill}\n"

        return result

    return "I don't know that yet."