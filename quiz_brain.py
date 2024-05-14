class QuizBrain:
    def __init__(self, q_list):
        self.list = q_list
        self.question_number = 0

    def next_question(self):
        q = self.list[self.question_number]
        self.question_number += 1
        guess = input(f"Q.{self.question_number}: {q.text} (True/False)?: ")
