# Assignment 1
# January 14, 2004

# Question 3
# Create a List L that is defined as= [10, 20, 30, 40, 50, 60, 70, 80].
#    (i) WAP to add 200 and 300 to L.
#    (ii) WAP to remove 10 and 30 from L.
#    (iii) WAP to sort L in ascending order.
#    (iv) WAP to sort L in descending order.

l = [10, 20, 30, 40, 50, 60, 70, 80]
print(f'Current List : {l}')

# (i)
l.append(200)
l.append(300)
print(f'Printing after appending : {l}')

# (ii)
l.remove(10)
l.remove(30)
print(f'Printing after Deleting : {l}')


# (iii)
length = len(l)
for i in range(length):
    for j in range(0,length-1):
        if(l[i]<l[j]):
            temp = l[i]
            l[i] = l[j]
            l[j] = temp
print(f'Printing after Sorting in Ascending Order : {l}')

# (iv)
for i in range(length):
    for j in range(0,length-1):
        if(l[i]>l[j]):
            temp = l[i]
            l[i] = l[j]
            l[j] = temp
print(f'Printing after Sorting in Descending Order : {l}')
