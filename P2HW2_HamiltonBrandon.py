# Brandon Hamilton
# 11/05/2026
# P2HW2
# This program collects six module grades, stores them in a list,
# and displays the lowest grade, highest grade, sum, and average.

# Pseudocode:
# 1. Get grades for Module 1 through Module 6.
# 2. Store all grades in a list.
# 3. Find the lowest grade using min().
# 4. Find the highest grade using max().
# 5. Find the sum of grades using sum().
# 6. Calculate the average.
# 7. Display results in the required format.

# Get grades from user
module1 = float(input("Enter grade for Module 1: "))
module2 = float(input("Enter grade for Module 2: "))
module3 = float(input("Enter grade for Module 3: "))
module4 = float(input("Enter grade for Module 4: "))
module5 = float(input("Enter grade for Module 5: "))
module6 = float(input("Enter grade for Module 6: "))

# Store grades in a list
module_grades = [module1, module2, module3, module4, module5, module6]

# Calculate results
lowest_grade = min(module_grades)
highest_grade = max(module_grades)
grade_sum = sum(module_grades)
average_grade = grade_sum / len(module_grades)

# Display results
print("\n------------Results------------")
print(f"Lowest Grade:      {lowest_grade}")
print(f"Highest Grade:     {highest_grade}")
print(f"Sum of Grades:     {grade_sum}")
print(f"Average:           {average_grade:.2f}")
print("--------------------------------")