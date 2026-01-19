def load_questions():
    return [
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Earth", "Mars", "Jupiter", "Venus"],
            "answer": "2"
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
            "answer": "4"
        },
        {
            "question": "Which programming language is used for web development?",
            "options": ["Python", "HTML", "C++", "Java"],
            "answer": "2"
        },
        {
            "question": "How many days are in a leap year?",
            "options": ["365", "364", "366", "367"],
            "answer": "3"
        },
        {
            "question": "What is the capital of Japan?",
            "options": ["Beijing", "Seoul", "Tokyo", "Bangkok"],
            "answer": "3"
        },
    ]


def ask_question(question_data, question_number):
    print(f"\nQuestion {question_number}: {question_data['question']}")

    for i, option in enumerate(question_data["options"], start=1):
        print(f"{i}. {option}")

    user_answer = input("Your answer (1-4): ")
    return user_answer


def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0


def run_quiz():
    questions = load_questions()
    score = 0
    question_number = 1

    print("Welcome to the Holton College Quiz!")
    print("Please answer with the letter (1, 2, 3, or 4) of your choice.")

    for q in questions:
        user_answer = ask_question(q, question_number)
        score += check_answer(user_answer, q["answer"])
        question_number += 1

    print(f"\nQuiz Complete! You scored {score} out of {len(questions)}.")
    print("Thank you for playing!")

run_quiz()
