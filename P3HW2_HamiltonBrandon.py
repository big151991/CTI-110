# ************************************************
# Name: Your Name
# Date: 11/17/2026
# Assignment: P3HW2_LastnameFirstname
# Description:
# This program calculates an employee's regular pay,
# overtime pay, and gross pay based on hours worked.
#
# Pseudocode:
# 1. Ask the user for employee name.
# 2. Ask for hours worked.
# 3. Ask for pay rate.
# 4. Determine if overtime was worked.
# 5. If hours > 40:
#       Calculate overtime hours.
#       Calculate regular pay.
#       Calculate overtime pay.
#    Else:
#       Overtime hours and overtime pay are 0.
#       Calculate regular pay.
# 6. Calculate gross pay.
# 7. Display all required results.
# ************************************************

# Get employee information
employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

# Calculate pay
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    regular_hours = 40

    regular_pay = regular_hours * pay_rate
    overtime_pay = overtime_hours * (pay_rate * 1.5)

else:
    overtime_hours = 0
    regular_pay = hours_worked * pay_rate
    overtime_pay = 0

# Calculate gross pay
gross_pay = regular_pay + overtime_pay

# Display results
print("---------------------------------------")
print("Employee name:", employee_name)
print()

print("Hours Worked    Pay Rate    OverTime    OverTime Pay    RegHour Pay    Gross Pay")
print("-------------------------------------------------------------------------------")

print(f"{hours_worked:<16.1f}"
      f"{pay_rate:<12.2f}"
      f"{overtime_hours:<12.1f}"
      f"{overtime_pay:<16.2f}"
      f"{regular_pay:<15.2f}"
      f"{gross_pay:.2f}")
