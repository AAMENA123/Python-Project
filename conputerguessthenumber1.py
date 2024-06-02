#the code is little different from the previous computer guesses the number game
import random
def computer_guess(x):
    low = 1
    high = x
    feedback =''
    while feedback != 'c':
       if low != high:
        guess = random.randint(low, high)
       else:
        guess = low
       feedback = input(f"Is {guess} high[h], low[l] or correct[c]") .lower()
       if feedback == 'h':
            high = guess-1
       elif feedback =='l':
            low = guess+1
    print(f"computer guessed your number, {guess}, corrrectly!")       

computer_guess(int(input(f"Enter the range you want computer to guess:")))             