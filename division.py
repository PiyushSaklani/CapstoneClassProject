
def divide():
    try:
        num1 = int(input("\nEnter the numerator: "))
        num2 = int(input("Enter the denominator: "))
        result = num1 / num2
        print("The result is:", result)
    except ValueError:
        print("Please enter valid integer values for numerator and denominator.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
