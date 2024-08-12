# Name:                         states.py
# Author:                       Michael Sineiro
# Date of latest revision:      8/12/2024
# Purpose:                      Uses a Dictionary w/ States and capitals to make a quiz.

import random

# Dictionary of U.S. states and their capitals
statesAndCapitals = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Hawaii": "Honolulu",
    "Idaho": "Boise",
    "Illinois": "Springfield",
    "Indiana": "Indianapolis",
    "Iowa": "Des Moines",
    "Kansas": "Topeka",
    "Kentucky": "Frankfort",
    "Louisiana": "Baton Rouge",
    "Maine": "Augusta",
    "Maryland": "Annapolis",
    "Massachusetts": "Boston",
    "Michigan": "Lansing",
    "Minnesota": "Saint Paul",
    "Mississippi": "Jackson",
    "Missouri": "Jefferson City",
    "Montana": "Helena",
    "Nebraska": "Lincoln",
    "Nevada": "Carson City",
    "New Hampshire": "Concord",
    "New Jersey": "Trenton",
    "New Mexico": "Santa Fe",
    "New York": "Albany",
    "North Carolina": "Raleigh",
    "North Dakota": "Bismarck",
    "Ohio": "Columbus",
    "Oklahoma": "Oklahoma City",
    "Oregon": "Salem",
    "Pennsylvania": "Harrisburg",
    "Rhode Island": "Providence",
    "South Carolina": "Columbia",
    "South Dakota": "Pierre",
    "Tennessee": "Nashville",
    "Texas": "Austin",
    "Utah": "Salt Lake City",
    "Vermont": "Montpelier",
    "Virginia": "Richmond",
    "Washington": "Olympia",
    "West Virginia": "Charleston",
    "Wisconsin": "Madison",
    "Wyoming": "Cheyenne"
}

# Function to get user input and format it properly
def getInput(prompt):
    return input(prompt).strip().title()

# Function for the quiz
def quiz(statesAndCapitals):
    correctCount = 0
    incorrectCount = 0
    incorrectStates = []
    states = list(statesAndCapitals.keys())
    random.shuffle(states)

    # Loop through each state and quiz the user
    for state in states:
        capital = statesAndCapitals[state]
        userInput = getInput(f"What is the capital of {state}? (or type 'quit' to exit): ")

        # Allow the user to quit the quiz
        if userInput.lower() == "quit":
            break

        if userInput == capital:
            print("Correct!")
            correctCount += 1
        else:
            print(f"Incorrect. The capital of {state} is {capital}.")
            incorrectCount += 1
            incorrectStates.append(state)

        continueQuiz = getInput("Do you want to continue? (yes/no): ").lower()
        if continueQuiz != "yes":
            break
    
    # Summary of quiz results
    print("\nQuiz Summary:")
    print(f"Correct answers: {correctCount}")
    print(f"Incorrect answers: {incorrectCount}")
    
    # Display the states the user missed
    if incorrectStates:
        print("States you missed:")
        for state in incorrectStates:
            print(f"- {state}: {statesAndCapitals[state]}")

    print("Thank you for playing!")

if __name__ == "__main__":
    quiz(statesAndCapitals)

