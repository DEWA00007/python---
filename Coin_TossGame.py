# Coin toss game
import random
print("------Welcome to Coin Toss Game!------")
user_coin = 100
is_running = True

while is_running:
    print(f"You have {user_coin} coins ")
    user_bet = int(input("Enter Your bet: "))

    if user_bet > user_coin:
        print("Insufficient coins !!")
    elif user_bet <=0:
        print("Invalid bet !! (Must be greater than 0)")  
    else:      
        print(f"Your bet is: {user_bet}")    

        choose = input("Choose Heads or Tails (H/T):").upper()
        if choose =='H' or choose =='T':
            print(f"You choosed: {choose}")
            computer_choice= ["H","T"]
            bot_generated = random.choice(computer_choice)
            print(f"I choosed: {bot_generated}")

            if choose == bot_generated:
                user_coin += user_bet
                print("🎉 You win !!")
                print(f"Congrats Now You have: {user_coin} ")
            else:
                user_coin -= user_bet
                print("😢 You Lose!!")   
                print(f"Now You have: {user_coin} left ") 
        else:
            print("Invalid (Choose H/T)")

        if user_coin == 0:
            print("💀 Game Over! You have no coins left.")
            break    

        again=input("Do You want to Play agian(Y/N): ").upper()   
        if again =='Y':
            pass 
        else:
            is_running = False
print()
print("Thanks for playing!")
print(f"You finished with {user_coin} coins.")            