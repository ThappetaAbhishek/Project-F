import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from backend.memory_service import *

print("\n========== MEMORY ==========\n")

print("Projects:")
print(get_projects())

print("\nSkills:")
print(get_skills())

print("\nGoals:")
print(get_goals())

print("\nProfile:")
print(get_profile("name"))