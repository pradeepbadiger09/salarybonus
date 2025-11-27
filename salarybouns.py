import sys

if len(sys.argv) == 2:
    script_name = sys.argv[0]
    salary = float(sys.argv[1])
    print("User provided salary:")
else:
    script_name = sys.argv[0]
    salary = 20000.0
    print("No input given - using default salary:")

bonus = salary * 0.10
total_salary = salary + bonus

print("Script Name:", script_name)
print("Salary:", salary)
print("Bonus Amount:", bonus)
print("Total Salary After Bonus:", total_salary)
