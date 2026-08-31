# Orlando Harris
# 30 August 2026
# P1HW2
# Travel Budget displays travel expenses
# Calculates your travel expenses

print("This program will calculate your travel expenses and remaining budget for your trip.")
print()


print("---------------Travel Expenses Addition and Subtraction--------------------")
print()

# Find your destination
destination = input("Enter your destination: ")
print(f"Destination: {destination}")


# Amount of money you have to spend your budget
budget = float(input("Enter your budget:  $"))
# Amount of money spent on gas
gas = float(input("Enter the amount of gas you will need:  $"))
# Amount of money spent on accommodation
accommodation = float(input("Enter the amount of money you will spend on accommodation:  $"))
# Amount of money spent on food
food = float(input("Enter the amount of money you will spend on food:  $"))

# Total expenses added then subtracted from budget to find remaining budget
total_expenses = gas + accommodation + food
remaining_budget = budget - total_expenses

print(f"Total Budget: ${budget:.2f}")
print(f"Total Expenses: ${total_expenses:.2f}")
print(f"Remaining Budget: ${remaining_budget:.2f}")
