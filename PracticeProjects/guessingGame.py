import random

num=random.randint(1, 10)

while True:
    guess=input("Pick a number between 1 to 10: ")
    guess=int(guess)
    if guess < num:
        print("TOO LOW!")
    elif guess > num:
        print("TOO HIGH!")
    else:
        print("YOU WON ! ! !")
        again=input("Do you want to play again? (y/n) ")
        if again == "y":
            num=random.randint(1, 10)
            guess = None
        else:
            print("Thank you for playing!")
            break