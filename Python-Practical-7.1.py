def add(a,b):
    print("Result:", a + b)

def sub(a,b):
    print("Result:", a - b)

def mul(a,b):
    print("Result:", a * b)

def div(a,b):
    print("Result:", a / b)

def mod(a,b):
    print("Result:", a % b)

while True:

    print("\n---- CALC MENU ----")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 6:
        break

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if choice == 1:
        add(a,b)

    elif choice == 2:
        sub(a,b)

    elif choice == 3:
        mul(a,b)

    elif choice == 4:
        div(a,b)

    elif choice == 5:
        mod(a,b)

    else:
        print("Invalid choice")