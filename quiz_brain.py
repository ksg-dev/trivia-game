class QuizBrain:
    def __init__(self, q_list):
        self.list = q_list
        self.question_number = 0
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.list)


    def next_question(self):
        q = self.list[self.question_number]
        self.question_number += 1
        guess = input(f"Q.{self.question_number}: {q.text} (True/False)?: ").lower().strip()
        self.check_answer(guess,q.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower().strip():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")