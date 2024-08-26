import random
def userChoice():
    while True:
        choice=input("enter Rock..Paper..Scicors..").lower()
        if choice in["rock","paper","scicor"]:
            return choice
        else:
            return "invalid choice"
def computerChoice():
    return random.choice(["rock","paper","scicor"])

def matchWinner(user_choice,computer_choice):
    if user_choice==computer_choice:
        return "match Tie!!!!"
    elif(user_choice=="rock" and computer_choice=="scicor")or \
            (user_choice=="paper" and computer_choice=="rock") or \
            (user_choice=="scicor" and computer_choice=="paper"):
                return "You Win the match"
    else:
        return "computer Win the match!!!!"

def playGame():
    print("let's play Rock Paper Sccior!!:")
    while True:
        user_choice=userChoice()
        computer_choice=computerChoice()
        print(f"you choose { user_choice}.computer choose { computer_choice}")
        print(matchWinner(user_choice,computer_choice))
        play_again=input("DO you want to play again (yes/no)").lower()
        if play_again !="yes":
            print("Thanks for playing!!!!")
            break

playGame()

