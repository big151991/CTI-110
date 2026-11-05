# Brandon Hamilton
# 11/05/2026
# P2LAB2
# This program uses a dictionary to store vehicle MPG
# values and calculates gallons of gas needed for a trip.

# Pseudocode:
# 1. Create a dictionary containing vehicle names and MPG values.
# 2. Create a variable that stores all dictionary keys.
# 3. Display the keys.
# 4. Ask the user to choose a vehicle.
# 5. Display the vehicle's MPG.
# 6. Ask the user how many miles they will drive.
# 7. Calculate gallons needed (miles / MPG).
# 8. Display gallons needed rounded to two decimal places.

vehicles = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

# Store and display keys
keys = vehicles.keys()
print(keys)

# Get vehicle from user
vehicle = input("\nEnter a vehicle to see its mpg: ")

# Display MPG
mpg = vehicles[vehicle]
print(f"\nThe {vehicle} gets {mpg} mpg.")

# Get miles to drive
miles = float(input("\nHow many miles will you drive? "))

# Calculate gallons needed
gallons_needed = miles / mpg

# Display result
print(f"\n{gallons_needed:.2f} gallon(s) of gas are needed to drive the {vehicle} {miles} miles.")