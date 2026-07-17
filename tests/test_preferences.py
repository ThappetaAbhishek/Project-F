import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from backend.memory_service import get_preference

print("Likes:", get_preference("likes"))
print("Favorite Color:", get_preference("favorite_color"))
print("Hobby:", get_preference("hobby"))