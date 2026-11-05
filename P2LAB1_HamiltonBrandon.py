# Brandon Hamilton
# 11/05/2026
# P2LAB1
# This program calculates the diameter, circumference,
# and area of a circle using a radius entered by the user.

# Pseudocode:
# 1. Get radius from the user as a float.
# 2. Calculate diameter.
# 3. Calculate circumference.
# 4. Calculate area.
# 5. Display the results with the required formatting.

import math

# Get radius from user
radius = float(input("Enter the radius of the circle: "))

# Calculate values
diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2
# Display results