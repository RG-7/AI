# Assignment 1
# January 14, 2004

# Question 3
# Write a Python program to check the validity of password input by users.
#   Validation:
#       At least 1 letter between [a-z] and 1 letter between [A-Z].
#       At least 1 number between [0-9].
#       At least 1 character from [$#@].
#       Minimum length 6 characters.
#       Maximum length 16 characters.

one_small_alpha = 0
one_captel_alpha = 0
one_number = 0
one_char = 0
min_len = 1
max_length = 1

def length(password):
    global min_len, max_length  # Declare as global
    length_of_password = len(password)
    if length_of_password < 6:
        min_len = 0
    elif length_of_password > 16:
        max_length = 0

def number(password):
    global one_small_alpha, one_captel_alpha, one_number, one_char
    for c in password:
        ch = ord(c)
        if ch in range(48, 58):
            one_number += 1
        elif ch in range(65, 91):
            one_captel_alpha += 1
        elif ch in range(97, 123):
            one_small_alpha += 1
        elif ch in (35, 36, 64):  # ASCII values for #, $, @
            one_char += 1

def validate(password):
    global one_small_alpha, one_captel_alpha, one_number, one_char, min_len, max_length
    one_small_alpha = 0
    one_captel_alpha = 0
    one_number = 0
    one_char = 0
    min_len = 1
    max_length = 1

    length(password)
    number(password)
    
    if one_small_alpha == 0 or one_captel_alpha == 0 or one_char == 0 or one_number == 0 or min_len == 0 or max_length == 0:
        print("Invalid password!")
    else:
        print("Valid password!")

while True:
    password = input("Enter your password: ")
    validate(password)
