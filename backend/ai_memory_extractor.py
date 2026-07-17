import os
import json

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

MODEL = "gemini-2.5-flash"


def extract_memory(message):

    prompt = f"""
Extract structured memories from this message.

Message:
{message}

Return ONLY valid JSON.

Format:

{{
    "projects": [],
    "skills": [],
    "goals": [],
    "facts": []
}}

Rules:

- Only extract information explicitly mentioned.
- Never invent anything.
- Return empty arrays if nothing is found.
"""

    try:

        response = client.models.generate_content(
            model=MODEL,
            contents=prompt
        )

        text = response.text.strip()

        if text.startswith("```"):
            text = text.replace("```json", "")
            text = text.replace("```", "").strip()

        return json.loads(text)

    except Exception:

        return {
            "projects": [],
            "skills": [],
            "goals": [],
            "facts": []
        }