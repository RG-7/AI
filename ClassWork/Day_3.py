# Day 3
# January 23, 2024
# 8 Puzzle Problem
# Not completed Yet

# Question 1

mylist = []

for row in range(0, 3):
    temp = []
    for col in range(0, 3):
        temp.append(input())
    mylist.append(temp)

for lst in mylist:
    print(lst)

def search_index(mylist, number):
    for i in range(0, 3):
        for j in range(0, 3):
            if mylist[i][j] == number:
                return [i, j]

print(search_index(mylist, 0))
