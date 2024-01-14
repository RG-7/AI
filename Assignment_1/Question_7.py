# Assignment 1
# January 14, 2004

# Question 7
#   (i) Write a function which takes principal amount, interest rate and time. This function returns compound interest. Call this function to print the output.
#   (ii) Save this function (as a module) in a python file and call it in another python file.

# (i)
principal_amount = int(input("Enter Principal Amount : "))
intrest_rate = int(input("Enter Intrest Rate : "))
time = int(input("Enter the time period : "))

def compound_intrest(principal_amount,intrest_rate,time):
    rate_decimal = intrest_rate / 100.0
    compounding_frequency = 1
    amount = principal_amount * (1 + rate_decimal / compounding_frequency) ** (compounding_frequency * time)
    compound_interest_amount = amount - principal_amount

    return compound_interest_amount

res = compound_intrest(principal_amount,intrest_rate,time)
print(f"Compound Intrest is : {res:.2f}")
