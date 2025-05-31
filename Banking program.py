
def show_balance ():
    print(f"Your balance is Rs {balance:.2f}")

def deposit():
    amount = float(input("Enter the amount to be deposited: "))

    if amount <= 0:
        print("The deposit is not accepted")
        return 0
    
    if amount > 0:
        return amount 

def withdraw():
    amount = float(input("Enter the amount you want to withdraw: "))

    if amount > balance:
        print("Not enough balance in your account")
        return 0 

    elif amount <= 0 :
        print("Please enter a valid amount") 
        return 0 
    else:
        return amount
    
def interest():
    rate = 9.7
    print("The standard interest for loan is 9.7%")
    
    principle = float(input("Please enter the amount: "))
    if principle <= 0:
        print("The principle amount should be greater than 0")
        return 
    
    time = int(input("Please enter the duration in years: "))
    if time <= 0:
        print("The duration cannot be less than 1")
        return

    Simple_interest = (principle * rate * time ) / 100 
    Total_value = principle + Simple_interest
    
    print(f"The interest is {Simple_interest:.2f}")
    print(f"The total amount to be paid {Total_value:.2f}")
    



balance = 0
is_running = True

while is_running:
    print("\nWelcome to the National Society Bank")
    print("1.Show balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Calculate Interest")
    print("5.Exit")

    choice = input("Enter the option you want to excute (1-5): ")

    if choice == '1':
        show_balance()
    elif choice == '2':
        balance += deposit()
    elif choice == '3':
        balance -= withdraw()
    elif choice == '4':
        interest()
    elif choice == '5':
        print("Thank you for banking with us !!!!!")
        is_running = False
    else:
        print("Please enter a valid option")
