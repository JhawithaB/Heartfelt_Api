from flask import Flask, jsonify
from flask_cors import CORS
import random
import os

app = Flask(__name__)
CORS(app)

trivia = [
    {"question":"Who’s the most influential person in your life?Why?"},
    {"question":"Where would you be if you hadn’t followed your dream?"},
    {"question":"What’s a red flag about you?"},
    {"question":"What’s changing in your life (for the better)?"},
]

@app.route("/")
def home():
    return "Trivia API Running"

@app.route("/api/trivia")
def get_trivia():
    return jsonify(trivia)

@app.route("/api/random")
def random_question():
    return jsonify(random.choice(trivia))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
