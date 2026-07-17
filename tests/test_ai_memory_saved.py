import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from backend.memory_service import (
    get_projects,
    get_skills,
    get_goals,
    get_facts
)

print("Projects:")
print(get_projects())

print("\nSkills:")
print(get_skills())

print("\nGoals:")
print(get_goals())

print("\nFacts:")
print(get_facts())