quiz = {
    "question1":{
        "question": "What is my peak rank?",
        "answer": "platinum 1"
    },
    "question2":{
        "question": "Who do I main in comp?",
        "answer": "chamber"
    },
    "question3":{
        "question": "What is my favorite map?",
        "answer": "ascent"
    },
    "question4":{
        "question": "What site do I typically set up on as KJ?",
        "answer": "b"
    },
    "question5":{
        "question": "Am I a vandal or phantom user?",
        "answer": "vandal"
    },
    "question6":{
        "question": "What map is my favorite to marshal on?",
        "answer": "breeze"
    },
    "question7":{
        "question": "Which agent do I refuse to unlock?",
        "answer": "raze"
    },
    "question8":{
        "question": "Which vandal skin has the best inspect?",
        "answer": "origin"
    },
    "question9":{
        "question": "Whose contract did I max out first?",
        "answer": "sage"
    },
    "question10":{
        "question": "What phantom skin am I trying to get in my store?",
        "answer": "spectrum"
    },
    "question11":{
        "question": "Who do I like playing the least?",
        "answer": "astra"
    }
}

def valo_quiz(dict):
    print("Welcome to the valorant quiz about saf!\nPlease be sure to correctly spell out your whole answer :)\n")
    score = 0
    letter_grade = ""
    for key, value in quiz.items():
        print(value['question'])
        answer = input('Answer: ')
        if answer.lower() == value['answer'].lower():
            print('Correct')
            score += 1;
            print("Score: ", score)
        else:
            print("Incorrect")
            print("The correct answer is: " + value['answer'])
            print("score: ", score)
        print("")
    grade = score / len(quiz) * 100.00
    if grade < 60:
        letter_grade = "F"
    elif grade < 70:
        letter_grade = "D"
    elif grade < 80:
        letter_grade = "C"
    elif grade < 90:
        letter_grade = "B"
    else:
        letter_grade = "A"
    print("Thank you for taking this quiz.\nWith a final score of", round(grade,2),"%, you earned a(n)", letter_grade, ".")
valo_quiz(quiz)