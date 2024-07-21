# Name:                         speedo.py
# Author:                       Michael Sineiro
# Date of latest revision:      7/21/2024
# Purpose:                      calculates cals burned at certain time intervals.

# Calculates the total calories burned
def calculateCaloriesBurned(minutes, ratePerMinute):
    return minutes * ratePerMinute

# Returns a list of time intervals
def timeInterval():
    return [1, 10, 15, 20, 25, 30]

# For loop function calculates and displays the calories burned for each time interval 
def kcalInterval(ratePerMinute, intervals):
    for minutes in intervals:
        calories = calculateCaloriesBurned(minutes, ratePerMinute)
        print(f"Calories burned in {minutes} minutes: {calories} kcal")

# Main program.
def main():
    ratePerMinute = 4.2
    intervals = timeInterval()
    kcalInterval(ratePerMinute, intervals)

# Call the main function when the script is run directly.
if __name__ == "__main__":
    main()
