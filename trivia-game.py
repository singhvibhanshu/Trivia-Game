import random

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
    questions_list = list(questions.keys())
    total_questions = 3
    score = 0

    selected_questions = random.sample(questions_list, total_questions)

    for index, question in enumerate(selected_questions):
        print(f"{index + 1}. {question}")
        user_answer = input("Your answer: ").lower().strip()
        correct_answer = questions[question]

        if user_answer == correct_answer.lower():
            print("Correct answer!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {correct_answer}.\n")
    print(F"Game Over! Your final score is: {score}/{total_questions}")

trivia_game()