from art import logo
import random, os

def clean_screen():
    '''clear the console screen'''
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For macOS and Linux
    else:
        os.system('clear')

difficulty = {
    'easy' : 10,
    'hard' : 5
}

# check if variable is valid number
def is_valid_number(variable):
    try:
        int_value = int(variable)
        return True
    except ValueError:
        return False
    
# get valid number inputs
def get_number_input(prompt):
    is_valid = False
    while not is_valid:
        num = input(prompt)

        if is_valid_number(num) and int(num) <= 100 and int(num) >= 1:
            is_valid = True
            return int(num)
        else:
            print("Invalid input. Please provide a valid number from 1 to 100 only.")    


def play_game():
    # logo
    print(logo)

    print("Welcome to the Number Guessing Game!")

    print("I'm thinking of a number between 1 and 100.")

    random_number = random.randint(1,100)

    # print(f"Psst the number is {random_number}")

    get_right_difficulty = False
    while not get_right_difficulty:
        difficulty_choice = input("\nChoose a difficulty. Type 'easy' or 'hard': ").lower()

        if difficulty_choice not in difficulty.keys():
            print("Invalid input.")
        else:
            get_right_difficulty = True
    
    attempts = difficulty[difficulty_choice]

    win_game = False  

    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")

        user_guess = get_number_input("Make a guess: ")

        if user_guess > random_number:
            print(f"{user_guess} is too high.")
            if (attempts - 1) != 0:
                print("Guess again.")
        elif user_guess < random_number:
            print(f"{user_guess} is too low.")
            if (attempts - 1) != 0:
                print("Guess again.")
        else:
            win_game = True
            break
        
        attempts -= 1
    
    if win_game == True:
        print(f"You got it! The answer is {random_number}.")
    else:
        print("Game over. You run out of attempts.")
        print(f"Please try again. The answer is {random_number}.")
