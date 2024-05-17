class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has(self):

        if self.question_number < len(self.question_list):
            return True
        else:
            False

    def next_qize(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You Got it Right")
            self.score += 1
        else:
            print(f"Its Wrong Correct answer is: {correct_answer}")

        print(f"Your Score is {self.score}/{self.question_number}")
        print("\n")