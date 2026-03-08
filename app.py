from flask import Flask, jsonify
from flask_cors import CORS
import random
import os

app = Flask(__name__)
CORS(app)

heart_questions = [
    {"question":"Who’s the most influential person in your life?Why?"},
    {"question":"Where would you be if you hadn’t followed your dream?"},
    {"question":"What’s a red flag about you?"},
    {"question":"What’s changing in your life (for the better)?"},
    {"question":"If you could receive closure from one person, who would it be?"},
    {"question":"What’s the most important characteristic you look for in a partner?"},
    {"question":"What question can’t you seem to find the answer to?"},
    {"question":"Past or present is there someone you wish you made reconciling with? If so, who and why?"},
    {"question":"Where have you felt most rejected?"},
    {"question":"Where have you felt most accepted?"},
    {"question":"What has been your most valuable life lesson?"},
    {"question":"If you could ask God, Life, The Angels, or Powers That Be any question (and receive a direct answer), what would it be?"},
    {"question":"What is your biggest regret?"},
    {"question":"How are you different now than you were 5 years ago?"},
    {"question":"If money were no object, what would you do with your life?"},
    {"question":"If you could relive one day of your life, which day would it be and why?"},
    {"question":"What is a moment in your life that truly humbled you?"}
]

@app.route("/")
def home():
    return "Heart Questions API Running"

@app.route("/api/heartfelts")
def get_heart_questions():
    return jsonify(heart_questions)

@app.route("/api/random")
def random_question():
    return jsonify(random.choice(heart_questions))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))