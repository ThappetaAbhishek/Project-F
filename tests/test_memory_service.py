import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from backend.memory_service import *

save_profile("name", "Abhi")
save_goal("Become an AI Engineer")
save_project("Project F")
save_skill("Python")

print("Name:", get_profile("name"))
print("Goals:", get_goals())
print("Projects:", get_projects())
print("Skills:", get_skills())