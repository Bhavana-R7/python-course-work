
#PYTHON INTERVIEW QUESTIONS
#QUESTIONS
questions = [
   
    "1. Which operator is used for exponentiation?",
    "2. What is the output of: 'Python'.lower()?",
    "3. Which function is used to open a file?",
    "4. Which method adds an item to a list?",
    "5. What is the output of: list(range(3))?",
    "6. Which of the following is a dictionary?",
    "7. What is the output of: 'A' * 3?",
    "8. Which module is used for mathematical functions?",
    "9. Which function converts a string to an integer?",
    "10. Which of the following is not a keyword in Python?",
    "11. Which operator is used for membership testing?",
    "12. What is the output of: print(5 > 3 and 2 < 1)?",
    "13. Which keyword is used to create an anonymous function?",
    "14. What is the output of: print(type({}))?",
    "15. Which of these is used to install external packages?",
    "16. Which built-in function is used to get user input?",
    "17. Which method removes and returns last item of a list?",
    "18. Which operator is used to compare object identity?",
    "19. What is the output of: print(bool(0))?",
    "20. Which method is used to get keys from a dictionary?",
    "21. What is the correct file extension for Python files?"
]

#options
options = [
 
    ["a) ^", "b) **", "c) //", "d) exp"],
    ["a) PYTHON", "b) python", "c) Python", "d) error"],
    ["a) open()", "b) file()", "c) fopen()", "d) read()"],
    ["a) append()", "b) insert()", "c) add()", "d) push()"],
    ["a) [0, 1, 2]", "b) [1, 2, 3]", "c) (0, 1, 2)", "d) range(3)"],
    ["a) {1: 'one', 2: 'two'}", "b) [1, 2, 3]", "c) (1, 2, 3)", "d) {1, 2, 3}"],
    ["a) 'AAA'", "b) 'A3'", "c) 333", "d) Error"],
    ["a) math", "b) random", "c) cmath", "d) statistics"],
    ["a) int()", "b) str()", "c) float()", "d) eval()"],
    ["a) pass", "b) lambda", "c) eval", "d) class"],
    ["a) in", "b) has", "c) with", "d) of"],
    ["a) True", "b) False", "c) None", "d) Error"],
    ["a) lambda", "b) func", "c) def", "d) function"],
    ["a) <class 'dict'>", "b) <class 'set'>", "c) <class 'list'>", "d) <class 'tuple'>"],
    ["a) pip", "b) package", "c) install", "d) module"],
    ["a) input()", "b) raw_input()", "c) scan()", "d) read()"],
    ["a) remove()", "b) pop()", "c) delete()", "d) discard()"],
    ["a) ==", "b) is", "c) equals", "d) same"],
    ["a) True", "b) False", "c) None", "d) Error"],
    ["a) values()", "b) keys()", "c) items()", "d) getkeys()"],
    ["a) .py", "b) .python", "c) .pt", "d) .txt"]
]

#Answers
Answers = [
    "b",  
    "b",  
    "a",  
    "a",  
    "a",  
    "a",  
    "a",  
    "a",  
    "a",  
    "c",  
    "a",  
    "b",  
    "a",  
    "a",  
    "a",  
    "a",  
    "b",  
    "b",  
    "b",  
    "b",  
    "a"   
]

#QUIZ GAME RANDOM
# Version 1: Simple Sequential Quiz

def run_quiz(questions, options, answers):
    print("🧪 Welcome to the Python Quiz Game!\n")
    score = 0

    for i in range(len(questions)):
        print(questions[i])
        for opt in options[i]:
            print(opt)

        user_answer = input("Your answer (a/b/c/d): ").strip().lower()
        if user_answer == answers[i]:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer: {answers[i]}\n")

    print(f"🎯 Final Score: {score}/{len(questions)}")
    if score == len(questions):
        print("🎉 Excellent! You nailed it!")
    elif score > len(questions)//2:
        print("👍 Good job! Keep practicing!")
    else:
        print("📚 Keep learning, you’ll get better!")

# Call function
# run_quiz(questions, options, answers)