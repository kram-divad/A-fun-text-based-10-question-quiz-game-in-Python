questions = [
    {
        "prompt": "What is the capital of Norway",
        "options": ["A. Oslo", "B. Bergen", "C. Trondheim", "D. Stavanger"],
        "answer": "A"
    },
    {
        "prompt": "Which language is primarily spoken in Brazil?",
        "options": ["A. Spanish", "B. Portuguese", "C. English", "D. French"],
        "answer": "B"
    },
    {
        "prompt": "Who directed the movie 'Inception'?",
        "options": ["A. Steven Spielberg", "B. Martin Scorsese", "C. Christopher Nolan", "D. Quentin Tarantino"],
        "answer": "C"
    },
    {
        "prompt": "Who composed the Shovel Knight soundtrack?",
        "options": ["A. Jake Kaufman", "B. Clark Aboud", "C. Christopher Larkin", "D. Yoko Shimomura"],
        "answer": "A"
    },
    {
        "prompt": "What is the largest insect in the world?",
        "options": ["A. Goliath Beetle", "B. Giant Weta", "C. Titan Beetle", "D. Hercules Beetle"],
        "answer": "C"
    },
    {
        "prompt": "In which book do we find the character 'Atticus Finch'?",
        "options": ["A. The Great Gatsby", "B. To Kill a Mockingbird", "C. The Catcher in the Rye", "D. Lord of the Flies"],
        "answer": "B"
    },
    {
        "prompt": "Which philosopher is known for the quote 'I think, therefore I am'?",
        "options": ["A. Voltaire", "B. Aristotle", "C. René Descartes", "D. Immanuel Kant"],
        "answer": "C"
    },
    {
        "prompt": "In what year did the Berlin Wall fall?",
        "options": ["A. 1987", "B. 1989", "C. 1991", "D. 1993"],
        "answer": "B"
    },
    {
        "prompt": "What is the main ingredient in traditional Japanese miso soup?",
        "options": ["A. Tofu", "B. Seaweed", "C. Miso paste", "D. Fish stock"],
        "answer": "C"
    },
    {
        "prompt": "If you have 3 apples and you take away 2, how many do you have?",
        "options": ["A. 1", "B. 2", "C. 3", "D. 5"],
        "answer": "B"
    }
]

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Your answer (A, B, C or D): ").upper()
        if answer == question["answer"]:
            print("You got it!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {question['answer']}.\n")


    print(f"You got {score} out of {len(questions)} correct!!")

run_quiz(questions)

input("Press Enter to exit...")

        
