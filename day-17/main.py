from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    question_variable = Question(q_text = question_text, q_answer = question_answer)
    question_bank.append(question_variable)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score is :{quiz.score}/{quiz.question_number}")