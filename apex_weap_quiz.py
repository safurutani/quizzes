class QuizQuestion:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


questionList = [
"1. Which gun cannot equip a barrel mod? \na) longbow\nb) g7 scout\nc) hemlock\nd) l-star\ne) 30-30 repeater\nAnswer: ",
"2. How many bullets does a volt have if equipped with a purple/gold energy mag?\na) 20\nb) 22\nc) 24\nd) 26\ne) 28\nAnswer: ",
"3. What hop-up does the sentinel use? \na) shatter caps\nb) deadeye tempo\nc) boosted loader \nd) hammerpoint\ne) turbocharger\nAnswer: ",
"4. What scope does the kraber have?\na) 6x-10x\nb) 6x-8x\nc) 4x-10x\nd) 4x-8x\ne) 4x-6x\nAnswer: ",
"5. How many marksman weapons are in the game?\na) 6\nb) 5\nc) 4\nd) 3\ne) 2\nAnswer: ",
"6. Which gun does not have an alternate firing mode?\na) hemlock\nb) R-301\nc) flatline\nd) triple take\ne) 30-30 repeater\nAnswer: ",
"7. What ammo type is used by the most guns?\na) light\nb) heavy\nc) energy\nd) sniper\ne) shotgun\nAnswer: ",
"8. Which of the following sights cannot be equipped on the bocek?\na) 1x\nb) 1x-2x\nc) 2x\nd) 3x\ne) 2x-4x\nAnswer: ",
"9. How many guns are in the care package rotations at a time?\na) 1\nb) 2\nc) 3\nd) 4\ne) 5\nAnswer: ",
"10. What is the only hitscan weapon in the game?\na) wingman\nb) havoc\nc) eva-auto\nd) triple take\ne) charge rifle\nAnswer: ",
"11. Which shotgun requires you to reload each bullet?\na) peacekeeper\nb) eva-auto\nc) mozambique\nd) mastiff\ne) none of the above\nAnswer: ",
]
questions = [
    QuizQuestion(questionList[0], "e"),
    QuizQuestion(questionList[1], "d"),
    QuizQuestion(questionList[2], "b"),
    QuizQuestion(questionList[3], "a"),
    QuizQuestion(questionList[4], "c"),
    QuizQuestion(questionList[5], "a"),
    QuizQuestion(questionList[6], "b"),
    QuizQuestion(questionList[7], "e"),
    QuizQuestion(questionList[8], "c"),
    QuizQuestion(questionList[9], "e"),
    QuizQuestion(questionList[10], "d")
]
def run_quiz(questionList):
    score = 0
    i = 0
    wrong = "Question(s) missed: "
    questions_wrong = []

#start of quiz and asking questions
    print("Apex Legends Weapons Quiz (Season 10)")
#    print("Please choose the best answer")
    print("________________________________________")
    for q in questionList:
        i += 1
        answer = input(q.prompt).lower()
        if answer == q.answer:
            score +=1
        else:
            questions_wrong.append( str(i))
        print()
#end of quiz and calculating results
    print("________________________________________")
    print("Quiz finished!")
    print("Score: " + str(100 * score/len(questions)) + "%")
    print("You answered " + str(score) + " question(s) correctly.")
    if len(questions_wrong) == 0:
        print("CONGRATULATIONS! You got a perfect score!")
    elif len(questions_wrong) == 1:
        print(wrong + questions_wrong[0])
    elif len(questions_wrong) > 1:
        for missed in questions_wrong:
            if missed == questions_wrong[0]:
                wrong += missed
            else:
                wrong += ", " + missed


        print(wrong)


run_quiz(questions)