# Brandon Hamilton
# November 4, 2026
# P1HW1
# This program performs exponent calculations and
# add/subtract calculations using user input.

print("-----Calculating Exponents-----")

base = int(input("Enter an integer as the base value: "))
exponent = int(input("Enter an integer as the exponent: "))

result = base ** exponent

print()
print(base, "raised to the power of", exponent, "is", result, "!!")

print()
print("-----Addition and Subtraction-----")

num1 = int(input("Enter a starting integer: "))
num2 = int(input("Enter an integer to add: "))
num3 = int(input("Enter an integer to subtract: "))

final_result = num1 + num2 - num3

print()
print(num1, "+", num2, "-", num3, "is equal to", final_result)