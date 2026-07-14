import random

Choices=['rock' , 'scissor' , 'paper']

CompPnts=0
UserPnts=0

while True:
    UserChoice=input("Enter The Choice  \n1.Rock \n2.Paper \n3.Scissor \n4.Exit \n...").lower()
    CompChoice=random.choice(Choices)
    if UserChoice == CompChoice.lower():
        print(f"It was a tie as your choices was {UserChoice} and Computers choice was {CompChoice}")
    elif (UserChoice == "paper" and CompChoice=="rock" ) or (UserChoice == "scissor" and CompChoice=="paper") or (UserChoice == "rock" and CompChoice=="scissor"):
        print(f"You won as your choices was {UserChoice} and Computers choice was {CompChoice}")
        UserPnts+=1
    elif (CompChoice == "paper" and UserChoice=="rock") or (CompChoice == "scissor" and UserChoice=="paper") or (CompChoice == "rock" and UserChoice=="scissor"):
        print(f"The Bot won as your choices was {UserChoice} and Computers choice was {CompChoice}")
        CompPnts+=1
    else:
        print("Invalid Choice")
    if CompPnts==10:
        print(f"Game Over the Bot won with points {CompPnts} and your points were {UserPnts}")
        break
    if UserPnts==10:
        print(f"Game Over you won with points {UserPnts} and your points were {CompPnts}")
        break
    if UserChoice.lower()=="exit":
        print(f"Your Points are {UserPnts} .. and bots Points are  {CompPnts} but no one won as you quited")
        break
    else:
        print("Invalid Choice")

print("Thanks for playing the game")