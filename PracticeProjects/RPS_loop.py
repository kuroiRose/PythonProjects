from random import randint

player_wins = 0
computer_wins = 0
winning_score = 3

while player_wins < winning_score and computer_wins < winning_score :
    print(f"Player score: {player_wins} Computer score: {computer_wins}")
    print("...Rock...")
    print("...Paper...")
    print("...Scissors...")
    
    player = input("Enter your move: ").lower()
    if player == "quit" or player == "q":
        break
    
    num=randint(0, 2)
    if num==0:
        computer="rock"
    elif num==1:
        computer="paper"
    else:
        computer="scissors"
        
    print(f"Computer plays {computer}")
    
    if player==computer:
        print("It's a tie!")
    elif player=="rock":
        if computer=="scissors":
            print("You win!")
            player_wins+=1
        elif computer=="paper":
            print("computer wins!")
            computer_wins+=1
    elif player=="paper":
        if computer=="rock":
            print("You win!")
            player_wins+=1
        elif computer=="scissors":
            print("computer wins!")
            computer_wins+=1
    elif player=="scissors":
        if computer=="paper":
            print("You win!")
            player_wins+=1
        elif computer=="rock":
            print("computer wins!")
            computer_wins+=1
    else:
        print("Please enter a valid move!")

if player_wins > computer_wins:
    print("CONGRATS, YOU WON !")
elif player_wins == computer_wins:
    print("IT'S A TIE !")
else:
    print("OH NO :( THE COMPUTER WON. . .")