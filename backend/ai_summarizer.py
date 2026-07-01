import os
import time

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

MODEL = "gemini-2.5-flash"


def summarize(question, tool_outputs):
    """
    Converts outputs from multiple tools into one
    natural answer.
    """

    prompt = f"""
You are Project F.

The user asked:

{question}

Tool outputs:

{tool_outputs}

Write one clean, accurate answer.

Rules:
- Do not mention tool names.
- Remove duplicates.
- Use simple English.
- Keep important facts.
- Summarize if needed.
"""

    retries = 3

    for attempt in range(retries):

        try:

            response = client.models.generate_content(
                model=MODEL,
                contents=prompt
            )

            return response.text.strip()

        except Exception as e:

            if attempt == retries - 1:
                return f"Summarizer Error: {e}"

            time.sleep(3)