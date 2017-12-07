#This program is designed to be a multi-function calculator.
AVERAGE = 1
MEDIAN = 2
MODE = 3
QUIT = 4
#This function displays a greeting and a blurb about the program when starting it.
def main():
    print("Booting The Calculator....")
    print("NOTE: This program requires that the statistics module be installed to function.")
    print("Welcome to The Calculator! This program is a multifunction calculator!")
    user_values()
 #This function runs the user input required to run the program.   
def user_values():
    global user_input
    user_input = []
    try:
        user_input = float(input("Please enter a number: "))
    except NameError:
        print("Invalid character")
    except SyntaxError:
        print("Invalid character")
    
    while user_input > 0:
        try:
            user_input = float(input('Please enter a value greater than or equal to zero: '))  
        except NameError:
            print("Invalid character")
            continue
        except SyntaxError:
            print("Invalid character")
            continue
    display_menu()
    
#This function displays the menu options.
def display_menu():
    choice = 0
    while choice != QUIT:
        print("Calculator Options")
        print("1) Calculate the average of a set of numbers")
        print("2) Calculate the median of a set of numbers")
        print("3) Calculate the mode of a set of numbers")
        print("4) Quit")
        try:
            choice = int(input("Enter your desired choice: "))
        except NameError:
            print("Invalid character")
            continue
        except SyntaxError:
            print("Invalid character")
            continue
            
        output = handle_choice(choice)
    
        if choice > 1:
            print("Invalid selection")
        elif choice > 4:
            print("Invalid selection")
        

#These functions handle the necessary calculations.
def hand_average(AVERAGE):
    import statistics
    print(statistics.mean([user_input]))
    
def hand_median(MEDIAN):
    import statistics
    print(statistics.median([user_input]))
    
def hand_mode(MODE):
    import statistics
    print(statistics.mode([user_input]))
 
#This function handles the responses to the menu choice.  
def handle_choice(choice):
    if choice == AVERAGE:
        return hand_average(AVERAGE)
    elif choice == MEDIAN:
        return hand_median(MEDIAN)
    elif choice == MODE:
        return hand_mode(MODE)
    elif choice == QUIT:
        print("Exiting the program... Have a nice day!")
    else:
        print("Invalid selection. Please try again.")
main()