from search import search

results = search("Python programming")

for i, result in enumerate(results, start=1):
    print(f"\nResult {i}")
    print("Title :", result["title"])
    print("Body  :", result["body"])
    print("URL   :", result["url"])