from FileReader import FileReader
from Leaderboard import Leaderboard


class Quiz:

    def __init__(self, quiz_source):
        self.quiz_source = quiz_source
        self.file_reader = FileReader(quiz_source)
        self.name = self.set_user_name()
        self.score = 0
        self.question_counter = 0
        self.allowed_answers = ["1", "2", "3", "4"]

    def set_user_name(self):
        """Ask for and validate the user's name."""
        name = self.ask_name()
        while not all(letter.isalpha() or letter.isspace() for letter in name) or all(letter.isspace() for letter in name):
            print("Invalid name. You must include at least one letter. Spaces are optional.")
            name = self.ask_name()
        return name

    def ask_name(self):
        """Prompt and assign user's name."""
        return input("Please enter your name: ").strip()

    def begin(self):
        """Begins the quiz. Line by line will be read and parsed into questions that the user will have to answer."""
        quiz_data = self.file_reader.read_content()
        print("Let the quiz begin! Please answer with a number (1-4).")
        for line in quiz_data:
            question_data = self.file_reader.parse_line(line)
            self.handle_question(question_data)  # Display question
            self.handle_answer(question_data)
        # Quiz over!
        self.end_quiz()

    def end_quiz(self):
        """Display necessary information, output summary file, and exit program."""
        print(f"You scored {self.score} out of {self.question_counter}.")
        leaderboard = Leaderboard(self.quiz_source)
        leaderboard.write(self.name, self.score)
        leaderboard.display()

    def handle_question(self, question_data):
        """Parse question data and display to screen"""
        self.question_counter += 1  # increment question number
        self.display_question(question_data)

    def handle_answer(self, question_data):
        """Ask question to the user using information passed through argument"""
        answer = self.get_answer(question_data)  # get answer and validate
        self.test_answer(question_data, answer)  # test answer and modify score

    def display_question(self, question_data):
        """Take raw question data and format in a readable manner."""
        print(f"""
        Q{self.question_counter}. {question_data[0]}
        1. {question_data[1]}
        2. {question_data[2]}
        3. {question_data[3]}
        4. {question_data[4]}
        """)

    def get_answer(self, question_data):
        """Prompt and validate a user's answer. Modify user score accordingly."""
        user_answer = self.prompt_answer()
        while not self.is_answer_valid(user_answer):  # validate answer
            print("Please answer with a digit from 1 to 4")
            user_answer = self.prompt_answer()
        return user_answer

    def test_answer(self, question_data, user_answer):
        """Compare user answer with correct answer and modify score accordingly"""
        question_data[5] = question_data[5].strip('\n')  # clean the answer string
        if user_answer == question_data[5]:
            self.score += 1
        return

    def prompt_answer(self):
        """Ask the user for an answer."""
        return input("Answer: ").strip(' \n\t\r')  # clean the answer

    def is_answer_valid(self, answer):
        """Return bool if answer is allowed."""
        return answer in self.allowed_answers
