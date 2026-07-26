# Python Banking Project

def show_balance():
  print(f"Your balance is ${balance:.2f}")



def deposite():
  amount=float(input("Enter an amount to be deposited: "))

  if amount<0:
    print("This is not a valid amount!!!!")
    return 0
  else:
    return amount
  
  
        
def withdraw():
  amt=float(input("Enter the amount to be withdrawn: "))
  if amt>balance:
     print("Insufficient Balance !")
     return 0
  elif amt<0:
        print("This is not a valid amount!!!!")
        return 0
  else:
        return amt

  
balance = 0
is_running = True

while is_running:
  print("1.Show balance: ")
  print("2.Deposite money: ")
  print("3.Withdraw money: ")
  print("4.Exit")

  choice =input("Enter your choice(1-4): ")

  if choice=='1':
    show_balance()
  elif choice =='2':
    balance += deposite()
  elif choice =='3':
     balance -= withdraw()
  elif choice =='4':
    is_running = False    
  else:
    print("That is not a valid choice ")

print("Thanks for using our service 😊")
