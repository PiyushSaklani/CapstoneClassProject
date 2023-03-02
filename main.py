import add,multiplication,subtraction,division
import area_of_circle,area_of_rectangle,area_of_triangle,area_square

while True:

    print("-"*40)

    print("\nWelcome to the calculator program\n")
    choice = int(input("Please select an operation : \n\t1. Addition\n\t2. Subtraction\n\t3. Multiplication\n\t4. Division\n\t5. Area of Square\n\t6. Area of Rectangle\n\t7. Area of Circle\n\t8. Area of Triangle\n\t9. Exit\n>>>"))
    if choice == 1:
        print("\nThe result is:", add.add())
    elif choice == 2:
        print("\nThe result is:", subtraction.subtract())
    elif choice == 3:
        print("\nThe result is:", multiplication.multiplication())
    elif choice == 4:
        print("\nThe result is:", division.divide())
    elif choice == 5:
        print("\nThe result is:", area_square.area_of_square())
    elif choice == 6:
        print("\nThe result is:", area_of_rectangle.rect())
    elif choice == 7:
        print("\nThe result is:", area_of_circle.calculate_circle_area())
    elif choice == 8:
        print("\nThe result is:", area_of_triangle.AOT())
    elif choice == 9:
        print("\n\t:)")
        break
    else:
        print("\nInvalid input..\nEnter again\t:(")