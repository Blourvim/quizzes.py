import json

from model.quizz import Question, Quiz, Result

def load_quiz(filename: str) -> Quiz:
    with open(filename, 'r') as f:
        data = json.load(f)
    
    questions = [Question(q["text"], q["answers"]) for q in data["questions"]]
    results = [Result(r["description"], r["threshold"]) for r in data["results"]]
    return Quiz("Which Bean Are You?", questions, results)
