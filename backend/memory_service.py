from backend.repository import *


# ---------- Profile ----------

def save_profile(key, value):
    save_key_value("profile", key, value)


def get_profile(key):
    return get_value("profile", key)


# ---------- Preferences ----------

def save_preference(key, value):
    save_key_value("preferences", key, value)


def get_preference(key):
    return get_value("preferences", key)


# ---------- Goals ----------

def save_goal(goal):
    save("goals", "goal", goal)


def get_goals():
    return get_all("goals", "goal")


# ---------- Projects ----------

def save_project(project):
    save("projects", "project", project)


def get_projects():
    return get_all("projects", "project")


# ---------- Skills ----------

def save_skill(skill):
    save("skills", "skill", skill)


def get_skills():
    return get_all("skills", "skill")


# ---------- Facts ----------

def save_fact(fact):
    save("facts", "fact", fact)


def get_facts():
    return get_all("facts", "fact")