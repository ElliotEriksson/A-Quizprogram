# Elliot Eriksson
# Teinf-20
# 2022-03-16
# Ett Quizprogram (resources)



# Classes
class Questions:

    def __init__(self, question : str, options : str, answer : str):
        self.question = question
        self.options = options
        self.answer = answer

    def get_question(self):
        return self.question

    def get_options(self):
        return self.options

    def correct_answer(self):
        return self.answer
    
    def save_question(self):
        options = ""
        for opt in self.options:
            options+=opt
            options+=", "
        return f"{self.question}/{options}/{self.answer}"


class Quiz:
    
    def __init__(self, name : str, questions : str, points : int):
        self.name = name
        self.questions = questions
        self.points = points

    def get_name(self):
        print(f"Välkommen till {self.name}")
    
    def get_questions(self):
        print(f"Denna quiz har {len(self.questions)} frågor\n")

    def get_points(self):
        print(f"Du har {self.points} poäng\n")

    def plus_points(self):
        self.points += 1


def create_quiz():
    quiz = []
    name = input("Vad ska quizen heta? ")
    amount = int(input("Hur många frågor vill du ha? "))
    for i in range(amount):
        options = []
        question = input("Frågan: ")
        how_many = int(input("Hur många alternativ vill du ha? "))
        for i in range(how_many):
            option = input("Skriv ETT alternativ: ")
            options.append(option)
        answer = input("Skriv in det rätta svar: ")        
        full_question = Questions(question, options, answer)
        quiz.append(full_question.save_question())
    with open(name + ".txt", "w", encoding="utf-8") as f:
        for list in quiz:
            f.write('%s\n' % list)


def add_to_quiz():
    quiz = []
    name = input("Vad heter quizen?")
    amount = int(input("Hur många frågor vill du lägga till? "))
    for i in range(amount):
        options = []
        question = input("Frågan: ")
        how_many = int(input("Hur många alternativ vill du ha? "))
        for i in range(how_many):
            option = input("Skriv ETT alternativ: ")
            options.append(option)
        answer = input("Skriv in det rätta svar: ")
        answer = answer.lower()
        answer = answer.capitalize()
        full_question = Questions(question, options, answer)
        quiz.append(full_question.save_question())
    with open(name + ".txt", "a", encoding="utf-8") as f:
            for list in quiz:
                f.write('%s\n' % list)