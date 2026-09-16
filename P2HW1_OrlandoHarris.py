# Orlando Harris
# 16 September 2026
# P2HW1
# This program calculates and displays travel expense


print("This program will calculate your travel expenses and remaining budget for your trip.")
print()



print()

# Find your location
Location = (input("Location: "))


# Your initial budget
initial_budget = float(input("Initial_Budget:  $"))


# Amount of money spent on gas
fuel = float(input("Fuel:  $"))


# Amount of money spent on accommodation
accommodation = float(input("Accommodation:  $"))


# Amount of money spent on food
food = float(input("Food:  $"))


# Total expenses added then subtracted from initial budget to find remaining budget
total_expenses = fuel + accommodation + food
remaining_balance = initial_budget - total_expenses

print("---------------Travel Expenses-------------------")
print(f"{'Location:':<20} {Location}")
print(f"{'Initial Budget:':<20} {f'${initial_budget:.2f}'}")
print(f"{'Fuel:':<20} {f'${fuel:.2f}'}")
print(f"{'Accommodation:':<20} {f'${accommodation:.2f}'}")
print(f"{'Food:':<20} {f'${food:.2f}'}")



print("------------------------------------------")
print()


print(f"Remaining Balance: ${remaining_balance:.2f}")