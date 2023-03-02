def divide():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 / num2
    except ValueError:
        print("Please enter valid integer values for numerator and denominator.")
    except ZeroDivisionError:
        print("\nError: division by zero")
        return None
    except ValueError:
        print("\nError: invalid input")
        return None
    else:
        print(f"{num1} / {num2} = {result}")
        return result