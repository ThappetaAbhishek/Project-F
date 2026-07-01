import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from backend.multi_decision_engine import decide_all
from backend.tool_executor import execute

query = "Who is Sundar Pichai and latest news about him"

intents = decide_all(query)

print(intents)

print()

print(execute(intents, query))