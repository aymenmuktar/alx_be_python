# daily_reminder.py

# Ask for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Validate input and loop until correct priority is given
while priority not in ['high', 'medium', 'low']:
    print("Invalid priority. Please enter high, medium, or low.")
    priority = input("Priority (high/medium/low): ").lower()

# Validate time_bound input
while time_bound not in ['yes', 'no']:
    print("Invalid input. Please enter yes or no.")
    time_bound = input("Is it time-bound? (yes/no): ").lower()

# Reminder message
match priority:
    case 'high':
        if time_bound == 'yes':
            print(f"\nReminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"\nNote: '{task}' is a high priority task. Plan to complete it as soon as possible.")
    case 'medium':
        if time_bound == 'yes':
            print(f"\nReminder: '{task}' is a medium priority task that should be done today.")
        else:
            print(f"\nNote: '{task}' is a medium priority task. Try to complete it this week.")
    case 'low':
        if time_bound == 'yes':
            print(f"\nReminder: '{task}' is a low priority task but needs to be done today.")
        else:
            print(f"\nNote: '{task}' is a low priority task. Consider completing it when you have free time.")

# Final message
print("\nWell done on completing this project! Let the world hear about this milestone achieved.\n🚀 Click here to tweet! 🚀")

