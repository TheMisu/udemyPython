class QuizBrain:
    def __init__(self, q_list):
        """
        Constructor for the QuizBrain class. It sets the question_number/score to 0 by default and sets the list of questions
        to a list we pass to the constructor.
        """
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        
    
    def next_question(self):
        """
        Method that selects the question at index question_number from question_list and asks the user for the answer
        """
        selected_q = self.question_list[self.question_number]
        self.question_number += 1
        
        user_answer = input(f"Q.{self.question_number}: {selected_q.text}. (True/False)?: ").lower()
        self.check_answer(user_answer, selected_q.answer)


    def still_has_questions(self):
        """
        Method that determines whether the quiz still has unanswered questions or not
        """
        return self.question_number < len(self.question_list)



    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}.")
        print("\n")