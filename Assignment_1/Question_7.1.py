# Assignment 1
# January 14, 2004

# Question 7 (ii)
#   (i) Write a function which takes principal amount, interest rate and time. This function returns compound interest. Call this function to print the output.
#   (ii) Save this function (as a module) in a python file and call it in another python file.

# (ii)
from Question_7 import compound_intrest

principal_amount = int(input("Enter Principal Amount : "))
intrest_rate = int(input("Enter Intrest Rate : "))
time = int(input("Enter the time period : "))

res = compound_intrest(principal_amount,intrest_rate,time)
print(f"Compound Intrest is : {res:.2f}")
