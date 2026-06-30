import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from tools.news import get_news

news = get_news("AI")

for i, item in enumerate(news, start=1):
    print(f"\n{i}. {item['title']}")
    print(item["link"])