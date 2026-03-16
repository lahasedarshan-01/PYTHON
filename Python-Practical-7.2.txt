balance = 1000

def show_balance():
    print("Current Balance:", balance)

def deposit():
    global balance
    amount = int(input("Enter amount to deposit: "))
    balance += amount
    print("Amount deposited successfully")

def withdraw():
    global balance
    amount = int(input("Enter amount to withdraw: "))

    if amount <= balance:
        balance -= amount
        print("Amount withdrawn successfully")
    else:
        print("Insufficient balance")

while True:

    print("\n--- BANK MENU ---")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        show_balance()

    elif choice == 2:
        deposit()

    elif choice == 3:
        withdraw()

    elif choice == 4:
        break

    else:
        print("Invalid choice")