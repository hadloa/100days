from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = [Question(i['text'], i['answer']) for i in question_data]
quiz_brain = QuizBrain(question_bank)
#[print(i.text, i.answer) for i in question_bank]

while quiz_brain.still_has_questions():
    quiz_brain.next_question()


print("You've completed the quiz!")
print(f"Your final score is {quiz_brain.score}/{quiz_brain.question_number}!\n")
