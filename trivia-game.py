import random  # Importing the random module to randomly select questions

# Dictionary containing trivia questions as keys and their correct answers as values
questions = {
    "What keyword is used to create a function in Python?": "def",
    "Which data type represents truth values in Python?": "bool",
    "What is the standard file extension for Python scripts?": ".py",
    "What character is used for single-line comments in Python?": "#",
    "Which function is used to receive user input in Python?": "input",
    "How do you initiate a loop that iterates over a sequence in Python?": "for",
    "What is the output of 3 ** 2 in Python?": "9",
    "Which keyword is used to include external modules in Python?": "import",
    "What does the type() function return?": "data type",
    "What is the result of 15 // 4 in Python?": "3"
}

def trivia_game():
    # Convert dictionary keys (questions) into a list
    questions_list = list(questions.keys())
    
    total_questions = 7  # Number of questions to ask
    score = 0  # Initialize score counter

    # Randomly select a specified number of questions from the list
    selected_questions = random.sample(questions_list, total_questions)

    # Iterate through selected questions
    for index, question in enumerate(selected_questions):
        print(f"{index + 1}. {question}")  # Display question number and question text
        user_answer = input("Your answer: ").lower().strip()  # Get user input, convert to lowercase, and remove spaces
        correct_answer = questions[question]  # Retrieve correct answer from dictionary

        # Check if user answer matches correct answer (case-insensitive)
        if user_answer == correct_answer.lower():
            print("Correct answer!\n")
            score += 1  # Increase score for correct answer
        else:
            print(f"Wrong! The correct answer is: {correct_answer}.\n")  # Show correct answer if incorrect

    # Display final score after the game ends
    print(f"Game Over! Your final score is: {score}/{total_questions}")

# Call the function to start the trivia game
trivia_game()
