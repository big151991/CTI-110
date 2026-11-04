# Brandon Hamilton
# November 4, 2026
# P1HW2
# This program calculates travel expenses and
# determines the amount of money remaining in the budget.

# Get the user's budget
budget = float(input("Enter Budget: "))

# Get the travel destination
destination = input("Enter your travel destination: ")

# Get estimated travel expenses
gas = float(input("How much do you think you will spend on gas? "))
accommodation = float(input("Approximately, how much will you need for accommodation/hotel? "))
food = float(input("Last, how much do you need for food? "))

# Calculate total expenses
expenses = gas + accommodation + food

# Calculate remaining budget
remaining_budget = budget - expenses

# Display results
print("\n------------Travel Expenses------------")
print("Location:", destination)
print("Initial Budget:", f"${budget:.2f}")
print("\nFuel:", f"${gas:.2f}")
print("Accommodation:", f"${accommodation:.2f}")
print("Food:", f"${food:.2f}")
print("---------------------------------------")
print("Remaining Balance:", f"${remaining_budget:.2f}")