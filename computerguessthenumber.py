# This program uses string concatenation
import random
def computer_guess(x):
    no = int(input(f"Enter the number you want computer to guess from 1 to {x}:"))
    guess = 0
    while guess != no:
        guess = random.randint(1, x)
        if guess < no:
            print(f"{guess} is low")
        elif guess> no:
            print(f"{guess} is high")
    print(f"The computer guessed your number, {guess}, correctly") 

    
    
computer_guess(int(input("Enter the range your want computer to guess:")))