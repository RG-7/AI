# Assignment 1
# January 14, 2004

# Question 1
# A class with 10 students wants to produce some information from the results of the four standard tests in Maths, Science, English and IT. 
# Each test is out of 100 marks. The information output should be the highest, lowest and average mark for each test and the highest, lowest and average mark 
# overall. Write a program in Python to complete this task.
number_of_student = 10
subjects = ['Maths','Science','English','IT']
sub = ['maths','sci','eng','it']
maths = [85, 92, 78, 95, 88, 70, 96, 82, 90, 87]
sci = [77, 88, 92, 69, 95, 81, 73, 90, 85, 94]
eng = [65, 78, 92, 87, 80, 95, 71, 88, 84, 90]
it = [89, 75, 93, 82, 96, 70, 84, 91, 88, 79]


def highest_marks(scores):
    high = scores[0]
    for marks in scores:
        if marks > high:
            high = marks
    return high

def lowest_marks(scores):
    lowest = scores[0]
    for marks in scores:
        if marks < lowest:
            lowest = marks
    return lowest

def avg_marks(scores):
    sum = 0
    for marks in scores:
        sum+= marks
    
    avg = sum/number_of_student

    return avg

max_in_maths = highest_marks(maths)
max_in_sci = highest_marks(sci)
max_in_eng = highest_marks(eng)
max_in_it = highest_marks(it)

min_in_maths = lowest_marks(maths)
min_in_sci = lowest_marks(sci)
min_in_eng = lowest_marks(eng)
min_in_it = lowest_marks(it)

avg_in_maths = avg_marks(maths)
avg_in_sci = avg_marks(sci)
avg_in_eng = avg_marks(eng)
avg_in_it = avg_marks(it)


for sub, subject in zip(sub,subjects):
    print(f'\n--------- {subject}-------------')
    print(f'Highest Marks in {subject} is {eval("max_in_" + sub)}')
    print(f'Average Marks in {subject} is {eval("avg_in_" + sub)}')
    print(f'Lowest Marks in {subject} is {eval("min_in_" + sub)}')
    
stu = [0] *number_of_student
for i in range(0,number_of_student):
    stu[i] = maths[i] + sci[i] + eng[i] + it[i]

overall_highest = highest_marks(stu)
overall_avg = lowest_marks(stu)
overall_lowest = avg_marks(stu)
print('\n------------ Overall Calculation ---------------')
print(f'Overall Highest Marks is : {overall_highest}')
print(f'Overall Average Marks is : {overall_avg}')
print(f'Overall Lowest Marks is : {overall_lowest}')
