# Name:                         speedo.py
# Author:                       Michael Sineiro
# Date of latest revision:      7/21/2024
# Purpose:                      Uses an If/else block that prints a message based on inputted speed.


# Function to get a positive integer from the user.
def getPosInt():
    while True:
        try:
            value = int(input("Enter your speed: "))
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

# Function to check the speed and print a message.
def checkSpeed(speed):
    if 24 <= speed <= 56:
        print("Speed is normal.")
    else:
        print("Speed is not normal.")

# Main program.
def main():
    speed = getPosInt()
    checkSpeed(speed)

# Call the main function when the script is run directly.
if __name__ == "__main__":
    main()
