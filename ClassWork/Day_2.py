# Day 2
# January 16, 2024

# defining function
def addition(a, b):
  print(a + b)

addition(2,3) # calling a function

# defining a function with return statement
def add(num1, num2):
  return num1 + num2
num1= 5
num2 = 7
sum_of_num1_num2 = add(num1, num2)
print(f'Sum of {num1} & {num2} = {sum_of_num1_num2}')

# Function for finding compund intrest 
def compound_intrest(principal_amount,intrest_rate, time,compounding_frequency):
  rate_decimal = intrest_rate/100.0
  amount = principal_amount * (1 + rate_decimal / compounding_frequency) ** (compounding_frequency * time)
  # compound_intrest_amount = amount - principal_amount

  return amount

principal = float(input("Enter the Principal amount : "))
intrest = float(input("Enter intrest rate : "))
time = float(input("Enter the time period : "))
c_f = float(input("Enter the Compounding Frequency : "))

c_i = compound_intrest(principal,intrest,time,c_f)
print(f'Compound Intrest = {c_i}')

# Calling function of one file to another i.e. Importing as a module
# Create a file "C_I.py". No Create anothe file "Calc.py".
# Paste all the function code of Compound Intrest in "C_I.py"
# Then write the below code in "Calc.py"
from C_I import compound_intrest

principal = float(input("Enter the Principal amount : "))
intrest = float(input("Enter intrest rate : "))
time = float(input("Enter the time period : "))
c_f = float(input("Enter the Compounding Frequency : "))

c_i = compound_intrest(principal,intrest,time,c_f)
print(f'Compound Intrest = {c_i}')

# Classes & Objects  in python
class triangle:
  # Constructor inside a class
  def __init__(self,base,height):
    # object created & initilised
    self.base = base 
    self.height = height
  def area(self):
    area = 0.5 * self.base * self.height
    return area


base_of_t = 4
height_of_t = 6
t = triangle(base_of_t,height_of_t)
area = t.area()
print(f'Area of triangle having base = {base_of_t} & height = {height_of_t} is {area}')

# Question 8
# (a)
class Resturant:
  def __init__(self,resturant_name,cuisine_type):
    self.resturant_name = resturant_name
    self.cuisine_type = cuisine_type
  def describe_resturant(self):
    print(f'Resutrant Name: - {self.resturant_name}\nCuisine Type - {self.cuisine_type}')
  def open_resturant(self):
    print("The resturant is open!")

res = Resturant("The Street Cafe","Indian")
res.describe_resturant()
res.open_resturant()

# ------ Completed --------
