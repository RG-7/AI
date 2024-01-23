# Day 2
# January 23, 2024
# Assignment 2

# Question 1

mylist_initial = []
mylist_goal = []

for row in range(0, 3):
    temp = []
    for col in range(0, 3):
        temp.append(input())
    mylist_initial.append(temp)

for lst in mylist_initial:
    print(lst)

for row in range(0, 3):
    temp = []
    for col in range(0, 3):
        temp.append(input())
    mylist_goal.append(temp)

for lst in mylist_goal:
    print(lst)

def search_index(mylist, number):
    for i in range(0, 3):
        for j in range(0, 3):
            if mylist[i][j] == str(number):
                return [i, j]


def move_up(mat):
  l = search_index(mat,0)
  row = l[0]
  col = l[1]
  if row !=0:
    mat[row][col],mat[row-1][col] =mat[row-1][col] ,mat[row][col]
    return mat
  else:
    return
