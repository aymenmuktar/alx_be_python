# daily_reminder.py

def get_priority():
    while True:
        priority = input("Priority (high/medium/low): ").strip().lower()
        if priority in {"high", "medium", "low"}:
            return priority
        print("Invalid input. Please enter high, medium, or low.")

def get_time_bound():
    while True:
        time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
        if time_bound in {"yes", "no"}:
            return time_bound
        print("Invalid input. Please enter yes or no.")

def main():
    task = input("Enter your task: ").strip()
    priority = get_priority()
    time_bound = get_time_bound()

    print()  # Add spacing before the reminder

    match priority:
        case "high":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
            else:
                print(f"Note: '{task}' is a high priority task. Make sure to schedule time for it soon.")
        case "medium":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a medium priority task that still requires attention today.")
            else:
                print(f"Note: '{task}' is a medium priority task. Try to fit it into your day.")
        case "low":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a low priority but time-sensitive task. Try not to delay it.")
            else:
                print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time


