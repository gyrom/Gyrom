from random import randint
from time import sleep


def check_if_in_range(number):
    number = int(number)
    if 1 <= number <= 20:
        return number
    else:
        print(f"{number} is not in the range.")
        raise ValueError



def play_guess_the_number():
    print('Welcome to Guess the Number!')
    print('You will need to guess the number that I chose!')
    print('Are you ready to play?')
    # define a random number
    lucky_number = randint(0, 20)
    print(lucky_number)
    # define number of turns
    turn = 0
    # start while loop - main game loop
    while turn < 5:
        chosen_number = input('Please pick a number (1-20):')
        try:
            val = int(chosen_number)
            check_if_in_range(chosen_number)
            if int(chosen_number) == lucky_number:
                print(f"Good job! the number is {lucky_number}")
                print("You Won!!")
                turn = 5
                break
            elif int(chosen_number) < lucky_number:
                print(f"{chosen_number} is too small")
                turn += 1
                print(f"you have {5 - turn} turns left!")
                sleep(1)
            elif int(chosen_number) > lucky_number:
                print(f"{chosen_number} is too big")
                turn += 1
                print(f"you have {5 - turn} turns left!")
                sleep(1)
        except ValueError:
            print("Please enter a valid number")
    else:
        print("Goodbye!")


play_guess_the_number()
