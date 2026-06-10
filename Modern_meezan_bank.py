def create_account():
    name = input("enter your name")
    if name == "":
        print("Create your account first")
        return "",0
    balance = 0
    print("Your name was created successfully",name)
    return name,balance


def check_balance(name,balance):
    if name == "":
        print("Create your account first")
    else:
        print("your current balance is",balance)
        print("your name is",name)


def Deposite(name,balance):
    if name == "":
        print("Create your account first")
        return balance
    

    try: 
        amount = int(input("Enter amount to deposite"))
    except ValueError:
        print("Plz Enter only digits")
        return balance
    
    if amount<=0:
        print("invalid amount")
        return balance
    
    balance += amount
    print("amount was successfully deposited which is:",balance)
    return balance
    


def Withdraw(name,balance):
    if name == "":
        print("Create your account first")
        return balance  
    
    try:
        amount = int(input("enter amount to be withdraw"))
    except ValueError:
        print("Plz Enter only digits")
        return balance  
    
    if amount <= 0:
        print("invalid amount")    
    elif amount <= balance: 
      balance -=amount
      print("your balance successfully withdraw and the remaining balance is:",balance)
      return balance
    else: 
          print("insuffficient balance")
    return balance


print("Welcome to the meezan bank")

name = ""
balance = 0

while True:
    print("\n1. Create Account")
    print("2. Check Balance")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice:"))
    except ValueError:
        print("enter your Valid Choice")
        continue

    if choice == 1:
        name,balance = create_account()


    elif choice == 2:
        check_balance(name,balance)

    elif choice == 3:
       balance = Deposite(name,balance)

    elif choice == 4:
       balance =  Withdraw(name,balance)

    elif choice == 5:
       print("Thanks for choosing us")
       break

    else:
        print("Plz enter valid choice")  
         

    

   
      



        





    