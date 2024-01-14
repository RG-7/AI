# Assignment 1
# January 14, 2004

# Question 2
# Write a Python Program to input basic salary of an employee and calculate its Gross salary according to the following:
# Basic Salary <= 10000 : HRA = 20%, DA = 80%
# Basic Salary <= 20000 : HRA = 25%, DA = 90%
# Basic Salary > 20000 : HRA = 30%, DA = 95%.

print('------- Calculating Gross Salary ----------')
basic_salary = int(input("Enter Basic Salary: "))

def gross_income(basic_salary, hra, da):
    hra_value = (hra / 100) * basic_salary
    da_value = (da / 100) * basic_salary
    gross_income_value = basic_salary + hra_value + da_value
    return gross_income_value

if basic_salary <= 10000:
    hra, da = 20, 80
elif basic_salary <= 20000:
    hra, da = 25, 90
else:
    hra, da = 30, 95

result = gross_income(basic_salary, hra, da)
print(f'Gross Income  = {result}')
