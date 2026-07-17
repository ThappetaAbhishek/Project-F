import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from backend.handlers.preference_handler import can_handle

print(can_handle("I like Pizza"))
print(can_handle("My favorite color is Blue"))
print(can_handle("My hobby is Coding"))