# Brandon Hamilton
# 11/05/2026
# P2HW1
# This program calculates travel expenses and displays
# the results in a formatted budget report.

# Pseudocode:
# 1. Get budget amount from user.
# 2. Get travel destination.
# 3. Get estimated gas expense.
# 4. Get estimated accommodation expense.
# 5. Get estimated food expense.
# 6. Calculate remaining balance.
# 7. Display results in a formatted table.

# Get user input
budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")

gas = float(input("How much do you think you will spend on gas? "))
hotel = float(input("Approximately, how much will you need for accommodation/hotel? "))
food = float(input("Last, how much do you need for food? "))

# Calculate remaining balance
remaining = budget - gas - hotel - food

# Display results
print("\n------------Travel Expenses------------")
print(f"{'Location:':20}{destination}")
print(f"{'Initial Budget:':20}${budget:.2f}")
print(f"{'Fuel:':20}${gas:.2f}")
print(f"{'Accommodation:':20}${hotel:.2f}")
print(f"{'Food:':20}${food:.2f}")
print("---------------------------------------")
print(f"{'Remaining Balance:':20}${remaining:.2f}")