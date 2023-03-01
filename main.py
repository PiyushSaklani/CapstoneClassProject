import add,multiplication,subtraction,division

while True:
    print("\nWelcome to the calculator program!")
    print("Please select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter your choice (1-5): "))
    print("="*40)
    if choice == 1:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = add.add(num1,num2)
        print("="*40)
        print("The result is:", result)
    elif choice == 2:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print("="*40)
        result = subtraction.subtract(num1,num2)
        print("The result is:", result)
    elif choice == 3:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = multiplication.multiplication(num1,num2)
        print("="*40)
        print("The result is:", result)
    elif choice == 4:
        division.divide()
    elif choice == 5:
        print("Exiting the calculator program...")
        break
    else:
        print("Invalid choice! Please select a valid option.")
    print("="*40)
