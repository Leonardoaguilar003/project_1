Total_gross = float(input("Enter the gross income: "))
deps = float(input("Enter the number of dependents: "))

income_total = ((Total_gross - 10000) - 3000 * deps) * 0.2

print(income_total)