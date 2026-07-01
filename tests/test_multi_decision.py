import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from backend.multi_decision_engine import decide_all

print(
    decide_all(
        "Who is Sundar Pichai and latest news about him"
    )
)