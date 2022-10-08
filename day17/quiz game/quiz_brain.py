class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def next_question(self):
        answer = (input(f'Q{self.question_number + 1}: {self.question_list[self.question_number].text} (True/False) '))
        answer = answer.lower().capitalize()
        if answer == 'T':
            answer = 'True'
        elif answer == 'F':
            answer = 'False'

        self.check_answer(answer)
        self.question_number += 1

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, answer):
        if self.question_list[self.question_number].answer == answer:
            print("You got it right!")
            self.score += 1
        else:
            print('That is incorrect')
        print(f'The correct answer is {self.question_list[self.question_number].answer}')
        print(f'Your current score is {self.score}/{self.question_number + 1}\n')
