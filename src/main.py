# Elliot Eriksson
# Teinf-20
# 2022-03-16
# Ett Quizprogram (main)

from resources import Questions, Quiz, add_to_quiz, create_quiz
from random import choice


def main():    
    answer = input("Vill du.. \n(1) Göra en ny quiz? \n(2) Lägga till på en gammal quiz? \n(3) Bara spela?\n")

    # Creating you own quiz
    if answer == "1":      
        create_quiz()

    # Adding questions to an existing quiz
    elif answer == "2":
        add_to_quiz()

    # Getting info from a txt file
    question_bank = []
    quiz_name = input("Vilken quiz vill du köra? ")
    with open(f"{quiz_name}.txt", "r", encoding="utf-8") as f:
        for line in f.readlines():
            attributes = line.split("/")
            question = Questions(attributes[0], attributes[1], attributes[2])
            question_bank.append(question)
    
    # The Game
    quiz = Quiz(quiz_name + " Quizen", question_bank, 0)
    round = 1
    print("\n\n")
    quiz.get_name()
    quiz.get_questions()


    while len(question_bank) != 0:
        current_question = choice(question_bank)
        print(f"[ Fråga {round} ]")
        print(current_question.get_question())
        print(current_question.get_options())    
        answer = input()  
        answer = answer.lower()
        answer = answer.capitalize()
        if answer in current_question.correct_answer():
            print("RÄTT!")
            quiz.plus_points()
            quiz.get_points()
        else:
            print(f"Fel, rätt svar är {current_question.correct_answer()}")
            quiz.get_points()
        question_bank.remove(current_question)
        round += 1
        
    print("\n\n")
    print(f"You ended with {quiz.get_points} points!")

if __name__ == "__main__":
    main()