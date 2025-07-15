#!/usr/bin/env python3
# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    """Displays the current date and time in YYYY-MM-DD HH:MM:SS format."""
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted_date)
    return current_date

def calculate_future_date(current_date, days_to_add):
    """Calculates and displays the future date after adding specified days."""
    future_date = current_date + timedelta(days=days_to_add)
    print("Future date:", future_date.strftime("%Y-%m-%d"))
    return future_date

if __name__ == "__main__":
    # Part 1: Display current date and time
    current_date = display_current_datetime()

    # Part 2: Ask user for days and calculate future date
    try:
        days_input = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(current_date, days_input)
    except ValueError:
        print("Invalid input! Please enter a valid integer number of days.")

