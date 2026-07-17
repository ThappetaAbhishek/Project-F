import os
import sys
import json

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from backend.ai_memory_extractor import extract_memory

message = """
I'm building an AI Resume Builder using React, Flask and PostgreSQL.
My goal is to become an AI Engineer.
"""

result = extract_memory(message)

print(json.dumps(result, indent=4))