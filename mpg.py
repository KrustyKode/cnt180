# Name:                         mpg.py
# Author:                       Michael Sineiro
# Date of latest revision:      7/13/2024
# Purpose:                      calculates MPG

# Prompts the user to enter a positive float.
def getPosFloat(prompt):
    while True:
        try:
            value = float(input(prompt))
            # with up to two decimal places.
            if value > 0 and len(str(value).split('.')[1]) <= 2:
                return value
            # validating inputs.
            else:
                print("Invalid input. Please enter a positive number up to two decimals long")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a positive number")

# Main method gets inputs.
def main():
    miles = getPosFloat("Enter the number of miles driven: ")
    gallons = getPosFloat("Enter the number of gallons of gas used: ")

    # calcs mpg.
    mpg = miles / gallons

    # prints the results.
    print(f"\nMiles driven: {miles:.2f}")
    print(f"Gallons used: {gallons:.2f}")
    print(f"Miles per gallon: {mpg:.2f}")

# dunder method checks if script is being called directly. 
if __name__ == "__main__":
    main()
