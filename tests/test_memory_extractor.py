import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from backend.memory_extractor import extract
from backend.memory_service import *

extract("I am building Smart Office System using React Flask Python")

print(get_projects())
print(get_skills())