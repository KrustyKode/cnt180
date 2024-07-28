# Name:                         ftToIn.py
# Author:                       Michael Sineiro
# Date of latest revision:      7/28/2024
# Purpose:                      Converts a user input from Ft. to In.
def main():
    feet = getFeetInput()  # Get user input
    inches = feetToInch(feet)  # Convert to inches
    print(f"{feet} feet is equal to {inches} inches.")  # Print result

def getFeetInput():
    while True:
        try:
            feet = float(input("Enter the number of feet: "))  # Read input
            if feet < 0:
                raise ValueError("The number of feet cannot be negative.")  # Check for negative input
            return feet
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid number.")  # Handle invalid input

def feetToInch(feet):
    inchesPerFoot = 12  # Conversion factor
    return feet * inchesPerFoot

if __name__ == "__main__":
    main()  # Run the program
