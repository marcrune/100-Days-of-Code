from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []

for item in question_data:
    question_bank.append(Question(item['text'], item['answer']))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
    quiz.check_answer
    quiz.question_number += 1

print("You've completed the quiz.")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")