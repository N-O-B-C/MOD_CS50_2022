import random

def main():
    number_guesting()
#This is number guessin game.
def number_guesting():
    try:
        gues_to = int(input("Enter a uper_value: "))
        guess_between = random.randint(1, gues_to)
    except ValueError:
        gues_to = int(input("Enter a uper_value: "))
        if gues_to < 1:
            gues_to = int(input("Enter a uper_value: "))
            guess_between = random.randint(1, gues_to)
    while True:
        try:
            guess = int(input("Guest: "))
            if guess_between == guess:
                print("Congratulation you got it right.")
                break
            elif guess > guess_between:
                print("Guess lower your guess is high.")
            elif guess < guess_between:
                print("Guest higher your guest is low.") 
            else:
                guess = int(input("Guest: "))
        except ValueError:
            print("The program only requires integer input.")
            guess = int(input("Guest: "))

main()