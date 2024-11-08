# Function to calculate total salary with HRA and TA
def calculate_total_salary(salary):
    hra = 0.10 * salary  # 10% of salary as HRA
    ta = 0.05 * salary   # 5% of salary as TA
    total_salary = salary + hra + ta
    return total_salary

# Accept salary from user
salary = float(input("Enter your basic salary: "))

# Calculate total salary
total_salary = calculate_total_salary(salary)

# Display the total salary
print(f"Your total salary with HRA and TA is: {total_salary}")
