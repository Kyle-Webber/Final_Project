#This program is designed to be a quiz, with three different 
#quiz options avaliable, along with a quit function.
APPLE_QUIZ = 1
GEORGRAPHY_QUIZ = 2
HISTORICAL_QUIZ = 3
QUIT = 4

#This function displays a greeting and a blurb about the program when starting it.
def main():
    print("Booting Kyle's Exquisite Quiz Game....")
    print("Welcome to Kyle's Exquisite Quiz Game! This program gives you the opprotunity to play a selection of quizzes based on various topics!")


#This function displays the menu options.
def display_menu():
    print("Quiz Options")
    print("1) Apple Quiz! (Hint: Not the fruit...)")
    print("2) Geography Quiz! Test your knowledge of geography!")
    print("3) History Quiz! Showcase your knowledge of our history!")
    print("4) Quit")

choice = 0
   
while choice != QUIT:
    display_menu()
    choice = int(input("Enter your desired choice: "))
    output = handle_choice(choice)
    
    if choice > 1:
        print("Invalid selection")
    elif choice > 4:
        print("Invalid selection")
    
def apple_quiz():
    import apple_quiz.py

def geography_quiz():
    import geography_quiz.py
    
def history_quiz():
    import history_quiz.py



    main()