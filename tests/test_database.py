import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from backend.database import initialize_database

initialize_database()

print("Database created successfully.")