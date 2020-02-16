from random import randint
from time import sleep

#this function checks if the user's number is in the range.
#we will use it later
def check_if_in_range(number):
    number = int(number)
    if 1 <= number <= 20:
        return number
    else:
        print(f"{number} is not in the range.")
        raise ValueError


chosen_numbers_list = []        

#this function checks if the user's number was already picked.
#we will use it later

def check_if_new_number(number):
    if number in chosen_numbers_list:
        print(f"you already chose {number}")
        raise ValueError
    else:
        chosen_number_list.append(number)
        return number

    
#this is the main game code
def play_guess_the_number():
    print('Welcome to Guess the Number!')
    print('You will need to guess the number that I chose!')
    print('Are you ready to play?')
    # define a random number
    lucky_number = randint(0, 20)
    # define number of turns
    turn = 0
    # start while loop - main game loop
    while turn < 5:
        chosen_number = input('Please pick a number (1-20):')
        try:
            #this is where we check to see if user really types number,
            #if it's in the range, and if he hadn't picked it before.
            check_if_in_range(chosen_number)
            check_if_new_number(chosen_number)
            
            #this is where we check if the user guessed correctly
            if int(chosen_number) == lucky_number:
                print(f"Good job! the number is {lucky_number}")
                print("You Won!!")
                turn = 5
                break
             
            #this is if the user guessed too small of a number
            elif int(chosen_number) < lucky_number:
                print(f"{chosen_number} is too small")
                turn += 1
                print(f"you have {5 - turn} turns left!")
                sleep(1)
            
            #this is if the user guessed too big of a number
            elif int(chosen_number) > lucky_number:
                print(f"{chosen_number} is too big!")
                turn += 1
                print(f"you have {5 - turn} turns left!")
                sleep(1)
                
        except ValueError:
            print("Please enter a valid number")
    else:
        print("Goodbye!")


play_guess_the_number()
