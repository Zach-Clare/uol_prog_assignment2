"""
### HOW TO USE ###
Simply run this file.
You will be prompted for a filename. The file you offer should contain a correctly formatted CSV file.
There should be quiz.txt and general_knowledge.txt provided with this project. 
I have created general_knowledge.txt as part of the stretch exercise.
Leaderboard files will be generated for each quiz.
"""

from Quiz import Quiz

# Ask user for a quiz source file to initialise from.
quiz_source = input("Please enter a quiz name: ")
quiz = Quiz(quiz_source)

# Begin the quiz! Everything will be handled from elsewhere from now.
quiz.begin()
