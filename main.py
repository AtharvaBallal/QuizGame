import question_model
import data
import quiz_brain

question_bank = []

for question in data.question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = question_model.Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = quiz_brain.QuizBrain(question_bank)
while quiz.still_has():
    quiz.next_qize()

print("You have completed quiz")
print(f"Your final score is : {quiz.score}/{quiz.question_number}")
