while True:
    task = input("Enter your task: ").strip()
    priority = input("Priority (high/medium/low): ").lower().strip()
    time_bound = input("Is it time-bound? (yes/no): ").lower().strip()

    # Validate inputs
    if priority not in ["high", "medium", "low"] or time_bound not in ["yes", "no"]:
        print("Invalid input. Please try again.\n")
        continue  # repeat loop if input is invalid
    else:
        break  # exit loop when inputs are valid

# Match-case to decide based on priority
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task."
    case "medium":
        reminder = f"'{task}' is a medium priority task."
    case "low":
        reminder = f"'{task}' is a low priority task."
    case _:
        reminder = f"'{task}' has an unknown priority."

# If time-bound, modify the reminder
if time_bound == "yes":
    reminder += " This requires immediate attention today!"
else:
    reminder += " Consider completing it when you have free time."

# Final reminder output
print("\nReminder:", reminder)
