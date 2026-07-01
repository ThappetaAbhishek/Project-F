import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from backend.ai_summarizer import summarize

answer = summarize(
    "Who is Sundar Pichai and latest news about him?",
    """
Wikipedia:
Sundar Pichai is the CEO of Google and Alphabet.

News:
Google announced major AI investments.
Pichai recently discussed the future of AI.
"""
)

print(answer)