import json

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) Paris", "B) Madrid", "C) Berlin", "D) Rome"],
        "answer": "A"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"],
        "answer": "B"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["A) Atlantic", "B) Indian", "C) Arctic", "D) Pacific"],
        "answer": "D"
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["A) Harper Lee", "B) Mark Twain", "C) J.K. Rowling", "D) George Orwell"],
        "answer": "A"
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": ["A) O2", "B) CO2", "C) H2O", "D) H2O2"],
        "answer": "C"
    }
]

def run_quiz():
    score = 0
    for q in questions:
        print(f"\n{q['question']}")
        for option in q['options']:
            print(option)
        answer = input("Your answer (A, B, C, or D): ").upper()
        
        if answer == q['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {q['answer']}.")
    
    print(f"\nQuiz completed! Your final score is {score}/{len(questions)}.")

def main():
    print("Welcome to the Quiz App!")
    start = input("Press Enter to start the quiz or type 'exit' to quit: ").lower()
    
    if start != 'exit':
        run_quiz()
    else:
        print("Goodbye!")

if __name__ == "__main__":
    main()
