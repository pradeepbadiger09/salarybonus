import sys

if len(sys.argv) != 2:
    print("Usage: python salary_bonus.py <salary>")
    sys.exit()

salary = float(sys.argv[1])
bonus = salary * 0.10
total = salary + bonus

print("Bonus Amount:", bonus)
print("Total Salary:", total)
