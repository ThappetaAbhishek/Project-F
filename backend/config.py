import os
from dotenv import load_dotenv

load_dotenv()

# ==========================
# AI Configuration
# ==========================

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = "gemini-2.5-flash"

# ==========================
# Search Configuration
# ==========================

SEARCH_MAX_RESULTS = 5

# ==========================
# Project Information
# ==========================

PROJECT_NAME = "Project F"
PROJECT_VERSION = "2.0"

# ==========================
# Memory Configuration
# ==========================

MAX_CONVERSATION_HISTORY = 20