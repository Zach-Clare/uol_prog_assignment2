import datetime


class Leaderboard:

    def __init__(self, quiz_name):
        """Save class attributes."""
        self.quiz_name = self.validate_quiz_name(quiz_name)
        self.file_name = f"{self.quiz_name}_leaderboard.txt"  # generate quiz-specific file name
        self.is_new = self.is_new()
        self.leaderboard_file = self.create_leaderboard()  # save file for this leaderboard

    def validate_quiz_name(self, quiz_name):
        """Ensure quiz name is valid alphanumeric text."""
        quiz_name = quiz_name.split(".")[0]  # remove extension from quiz's filename
        if all(letter.isalnum() or letter == "_" or letter == "-" for letter in quiz_name):  # validate
            return quiz_name
        return False

    def is_new(self):
        """Check if leaderboard file already exists."""
        try:
            f = open(self.file_name)  # attempt to open leaderboard file
            f.close()
        except FileNotFoundError:
            return True  # leaderboard file for this quiz does not exist therefore is new
        return False

    def create_leaderboard(self):
        """Format a new leaderboard file for this quiz if it doesn't exist already."""
        f = open(self.file_name, "a+")  # open with intent to append
        f.seek(0)  # Seek to beginning of file
        content = f.read()
        if self.is_new or len(content) == 0:  # if file does not exist or has no content
            f.write("Name,Score,Date,Time\n")
        return f  # if file already exists and has content, return fileObject

    def write(self, name, score):
        """Save quiz attempt data to quiz leaderboard file"""
        current_datetime = datetime.datetime.now()  # get date and time values
        date = current_datetime.strftime("%d/%m/%Y")  # format date
        time = current_datetime.strftime("%H:%M:%S")  # format time
        self.leaderboard_file.seek(0, 2)  # seek to end of file
        self.leaderboard_file.write(f"{name},{score},{date},{time}\n")  # write attempt data to file
        self.leaderboard_file.close()

    def display(self):
        """Format and display leaderboard"""
        f = open(self.file_name, "r")  # open leaderboard file
        results = f.readlines()  # get file contents
        header = results.pop(0)  # remove the top line (which will be the headers)
        leaderboard_data = list()  # using a container for leaderboard data will allow us to format it
        for result in results:
            leaderboard_data.append(result.split(","))  # put contents in our container
        # sort multidimensional list by second element of each
        leaderboard_data = sorted(leaderboard_data, key=lambda x: x[1], reverse=True)
        leaderboard_data.insert(0, list(header.split(",")))  # add headers at beginning of leaderboard
        column_max = self.get_column_max_values(leaderboard_data)  # get column widths
        for line in leaderboard_data:  # format data in leaderboard
            name = "| " + line[0] + (column_max[0] - len(line[0])) * " "  # add pipes, content, and calculate padding
            score = "| " + line[1] + (column_max[1] - len(line[1])) * " "
            date = "| " + line[2] + (column_max[2] - len(line[2])) * " "
            time = "| " + line[3].strip("\n") + (column_max[3] - len(line[3])) * " " + "|"
            print(name, score, date, time)  # display formatted line onto leaderboard

    def get_column_max_values(self, leaderboard_data):
        """Calculate column widths for leaderboard."""
        column_max = [0, 0, 0, 0]
        padding = 2  # we use padding between columns to make results more readable
        for row in leaderboard_data:  # iterate through each result
            # keep a track of how wide we'll need to make each column.
            column_max[0] = max(len(row[0]) + padding, column_max[0])
            column_max[1] = max(len(row[1]) + padding, column_max[1])
            column_max[2] = max(len(row[2]) + padding, column_max[2])
            column_max[3] = max(len(row[3]) + padding, column_max[3])
        return column_max
