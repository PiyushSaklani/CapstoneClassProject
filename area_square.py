
def area_of_square():
    try:
    # Ask user for input
        length = float(input("Enter the length of one side of the square: "))
        
        if (length<0):
            print("Length cannot be negative")
        else:   
            # Calculate area
            area = length ** 2
            
            # Print the area
            print("The area of the square is:", area)
        
    except ValueError:
        # Handle if user enters invalid input
        print("Invalid input. Please enter a number.")
    except:
        # Handle any other unexpected errors
        print("An error occurred.")
