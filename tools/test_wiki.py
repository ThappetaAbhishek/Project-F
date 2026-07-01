import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from tools.wiki import get_summary

result = get_summary("Alan Turing")

print(result)