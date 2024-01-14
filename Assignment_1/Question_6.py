# Assignment 1
# January 14, 2004

# Question 6
# WAP to create a list of 100 random numbers between 100 and 900. Count and print the:
#   (i) All odd numbers
#   (ii) All even numbers
#   (iii) All prime numbers
import random as rand

l = [rand.randint(100, 900) for _ in range(100)]
print(f"List is {l}")

# (i)
count_of_odd = 0
odd_list = []
for i in l:
    if(i%2!=0):
        odd_list.append(i)
        count_of_odd += 1
print(f'Total Number of Odd Numbers in List is {count_of_odd}')
print(f'List of all odd numbers : {odd_list}')

# (ii)
count_of_even = 0
even_list = []
for i in l:
    if(i%2==0):
        even_list.append(i)
        count_of_even += 1
print(f'Total Number of Even Numbers in List is {count_of_even}')
print(f'List of all even numbers : {even_list}')

# (iii)
count_of_prime = 0
prime_list = []
for num in l:
    if num < 2:
        break;
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            break;
    else:
        prime_list.append(num)
        count_of_prime += 1
print(f'Total Number of Prime Numbers in List is {count_of_prime}')
print(f'List of all prime numbers : {prime_list}')
