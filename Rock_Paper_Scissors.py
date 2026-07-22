# Rock paper scissor game !! 

import random 
options=("rock","paper","scissors")
is_running = True

while is_running:
    player = None
    computer = random.choice(options)

    while player not in options:   # this means it will not accept the option that is not in the option tuple!
            player=input("Enter a choice (rock,paper,scissors): ")

    print(f"Player:{player}")    
    print(f"Computer:{computer}")   

    if player == computer:
            print("It's a tie !")
    elif player== "rock" and computer =="paper":
            print("You lose!")
    elif player== "paper" and computer =="scissors":
            print("You lose!")        
    elif player== "scissors" and computer =="rock":
            print("You lose!")    
    else:
        print("You WIN  !! ")  
    play_again=input("Play again?(y/n)").lower()
    if play_again =="n":
       is_running=False   # this will stop the while loop  and exist
  
print("Thanks For playing!!")        
