# ************************************************
# Name: Your Name
# Date: 11/17/2026
# Assignment: P3HW1_HamiltonBrandon
# Description:
# This program takes six module grades,
# determines the lowest grade, highest grade,
# sum of grades, average grade, and letter grade.
#
# Pseudocode:
# 1. Get grades for six modules.
# 2. Store grades in a list.
# 3. Find the lowest grade.
# 4. Find the highest grade.
# 5. Find the sum of the grades.
# 6. Calculate the average.
# 7. Determine the letter grade.
# 8. Display the results.
# ************************************************

# Enter grades for six modules
mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# Add grades entered to a list
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# Determine lowest, highest, sum, and average
low = min(grades)
high = max(grades)
total = sum(grades)
avg = total / len(grades)

# Determine letter grade for average
if avg >= 90:
    letter_grade = "A"
elif avg >= 80:
    letter_grade = "B"
elif avg >= 70:
    letter_grade = "C"
elif avg >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

# Display results
print("\n------------Results------------")
print(f"Lowest Grade: {low}")
print(f"Highest Grade: {high}")
print(f"Sum of Grades: {total}")
print(f"Average: {avg:.2f}")
print(f"Letter Grade: {letter_grade}")
