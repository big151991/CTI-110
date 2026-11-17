# **************************************************************
# Name: Your Name
# Date: 11/17/2026
# Assignment: P3LAB_LastnameFirstname
# Description:
# This program accepts a money amount from the user and
# calculates the minimum number of dollars, quarters,
# dimes, nickels, and pennies needed to make that amount.
#
# Pseudocode:
# 1. Get money amount from user.
# 2. Convert amount to cents.
# 3. Calculate dollars using floor division.
# 4. Subtract dollars from total cents.
# 5. Calculate quarters and subtract.
# 6. Calculate dimes and subtract.
# 7. Calculate nickels and subtract.
# 8. Remaining cents are pennies.
# 9. Display only denominations that are needed.
# 10. Use singular/plural coin names correctly.
# **************************************************************

money = float(input("Enter the amount of money as a float: "))

# Convert to cents
cents = int(round(money * 100))

print()

# Dollars
dollars = cents // 100
cents = cents - (dollars * 100)

# Quarters
quarters = cents // 25
cents = cents - (quarters * 25)

# Dimes
dimes = cents // 10
cents = cents - (dimes * 10)

# Nickels
nickels = cents // 5
cents = cents - (nickels * 5)

# Pennies
pennies = cents

# Display results
if dollars > 0:
    if dollars == 1:
        print("1 Dollar")
    else:
        print(f"{dollars} Dollars")

if quarters > 0:
    if quarters == 1:
        print("1 Quarter")
    else:
        print(f"{quarters} Quarters")

if dimes > 0:
    if dimes == 1:
        print("1 Dime")
    else:
        print(f"{dimes} Dimes")

if nickels > 0:
    if nickels == 1:
        print("1 Nickel")
    else:
        print(f"{nickels} Nickels")

if pennies > 0:
    if pennies == 1:
        print("1 Penny")
    else:
        print(f"{pennies} Pennies")
    