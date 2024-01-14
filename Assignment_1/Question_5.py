# Assignment 1
# January 14, 2004

# Question 5
# D is a dictionary defined as D= {1:”One”, 2:”Two”, 3:”Three”, 4: “Four”, 5:”Five”}.
#   (i) WAP to add new entry in D; key=6 and value is “Six”
#   (ii) WAP to remove key=2.
#   (iii) WAP to check if 6 key is present in D.
#   (iv) WAP to count the number of elements present in D.
#   (v) WAP to add all the values present D.

D = {
    1 : "One",
    2 : "Two",
    3 : "Three",
    4 : "Four",
    5 : "Five"
}

print(f'\nDictonary : {D}')

# (i)
D.update({6:"Six"})
print(f'\nPrinting Dictonary after appending : {D}')

# (ii)
if 2 in D:
    del D[2]
print(f'\nPrinting Dictonary after Deleting 2 : {D}')


# (iii)
key_in_D = 6 in D
print(f'\n6 present in {D} : {key_in_D}')

# (iv)
n_o_e_in_D = len(D)
print(f'\nNo of Elements in D is {n_o_e_in_D}')

# (v)
sum_of_keys_of_D = 0
for keys in D.keys():
    key = int(keys)
    sum_of_keys_of_D += key
print(f'\nSum of Values in D is {sum_of_keys_of_D}')
