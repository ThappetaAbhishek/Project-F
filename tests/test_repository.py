import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from backend.memory_service import *

save_project("Project F")
save_project("AI Resume Builder")

save_skill("Python")
save_skill("Flask")
save_skill("React")

save_goal("Become AI Engineer")

print(get_projects())
print(get_skills())
print(get_goals())