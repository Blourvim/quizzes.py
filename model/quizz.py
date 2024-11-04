from typing import List, Dict, Union

class Question:
    def __init__(self, text: str, answers: List[Dict[str, Union[int, str]]]):
        self.text = text
        self.answers = answers  # list of answer dicts

    def __str__(self) -> str:
        answers_str = "\n".join(f"{ans['id']}: {ans['text']}" for ans in self.answers)
        return f"Question: {self.text}\nAnswers:\n{answers_str}"

class Result:
    def __init__(self, description: str, threshold: int):
        self.description = description
        self.threshold = threshold  # Minimum score needed to achieve this result
    def return_treshold(self)-> int:
        return self.threshold

    def __str__(self) -> str:
        return f"Result: {self.description} (Threshold: {self.threshold})"

class Quiz:
    def __init__(self, title: str, questions: List[Question], results: List[Result]):
        self.title = title
        self.questions = questions
        results.sort(reverse=True, key=Result.return_treshold)
        self.results = results

    def evaluate(self, selected_answers: List[Dict[str, Union[int, str]]]) -> Union[Result, str]:
        # Calculate the total score based on selected answer IDs
        total_score = sum(int(answer["id"]) for answer in selected_answers)  # Ensure that id is treated as int
        
        # Find the highest qualifying result based on thresholds
        for result in self.results:
            if total_score >= result.threshold:
                return result
        
        return "No matching result found."

    def __str__(self) -> str:
        questions_str = "\n\n".join(str(q) for q in self.questions)
        return f"Quiz: {self.title}\n\n{questions_str}"
