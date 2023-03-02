import add,multiplication,subtraction,division
import area_of_circle,area_of_rectangle,area_of_triangle,area_square

while True:

    print("\nWelcome to the calculator program\n")
    choice = int(input("Please select an operation : \n\t1. Addition\n\t2. Subtraction\n\t3. Multiplication\n\t4. Division\n\t5. Area of Square\n\t6. Area of Rectangle\n\t7. Area of Circle\n\t8. Area of Triangle\n\t9. Exit"))



    choice = int(input("Enter your choice (1-6): "))
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
        area_square.area_of_square()
    
    elif choice == 6:
        print("Exiting the calculator program...")
        break
    else:
        print("Invalid choice! Please select a valid option.")
    print("="*40)
