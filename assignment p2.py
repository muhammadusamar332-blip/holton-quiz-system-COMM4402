# Holton College Digital Quiz System
# Author: Muhammad Usama Riaz
# Student ID: 2425477

def load_questions():
    """
    Stores all quiz questions in a list of dictionaries.
    Each dictionary contains the question, options and correct answer.
    """
    return [
        {
            "question": "What is the capital of France?",
            "options": ["London", "Paris", "Berlin", "Madrid"],
            "answer": "2"
        },
        {
            "question": "Which data structure uses key-value pairs?",
            "options": ["List", "Tuple", "Dictionary", "Set"],
            "answer": "3"
        },
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": ["def", "func", "define", "function"],
            "answer": "1"
        },
        {
            "question": "Which of these is a loop in Python?",
            "options": ["if", "for", "break", "pass"],
            "answer": "2"
        },
        {
            "question": "Which symbol is used for comments in Python?",
            "options": ["//", "#", "/*", "<!--"],
            "answer": "2"
        }
    ]


def display_question(question_data, question_number):
    """Displays a single question and its options."""
    print(f"\nQuestion {question_number}: {question_data['question']}")
    for i in range(len(question_data["options"])):
        print(f"{i + 1}. {question_data['options'][i]}")


def get_user_answer():
    """Gets and validates user input."""
    answer = input("Your answer (1-4): ")
    while answer not in ["1", "2", "3", "4"]:
        print("Invalid input. Please enter 1, 2, 3, or 4.")
        answer = input("Your answer (1-4): ")
    return answer


def check_answer(user_answer, correct_answer):
    """Checks if the user's answer is correct."""
    if user_answer == correct_answer:
        print("Correct!")
        return True
    else:
        print("Wrong!")
        return False


def run_quiz():
    """Main function that runs the quiz."""
    questions = load_questions()
    score = 0

    print("Welcome to the Holton College Quiz!")
    print("Please answer with 1, 2, 3, or 4.")

    for i in range(len(questions)):
        display_question(questions[i], i + 1)
        user_answer = get_user_answer()

        if check_answer(user_answer, questions[i]["answer"]):
            score += 1

    print("\nQuiz Complete!")
    print(f"You scored {score} out of {len(questions)}")
    print("Thank you for playing!")


# Start the quiz
run_quiz()
