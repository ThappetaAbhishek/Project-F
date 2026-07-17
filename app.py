from flask import Flask, request, jsonify
from flask_cors import CORS

from backend.brain import get_response
from backend.memory_extractor import extract
from backend.ai_memory_extractor import extract_memory
from backend.memory_service import (
    save_project,
    save_skill,
    save_goal,
    save_fact
)
from memory.memory import remember

app = Flask(__name__)
CORS(app)


def save_ai_memory(data):
    for project in data.get("projects", []):
        save_project(project)

    for skill in data.get("skills", []):
        save_skill(skill)

    for goal in data.get("goals", []):
        save_goal(goal)

    for fact in data.get("facts", []):
        save_fact(fact)


@app.route("/")
def home():
    return jsonify({
        "name": "Project F API",
        "status": "running"
    })


@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"error": "Message is required"}), 400

    user = data["message"]

    # Existing extractor
    extract(user)

    # AI memory extractor
    memory = extract_memory(user)
    save_ai_memory(memory)

    # AI response
    response = get_response(user)

    # Save conversation
    remember(user, response)

    return jsonify({
        "reply": response
    })


if __name__ == "__main__":
    app.run(debug=True)