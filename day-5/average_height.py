student_heights = input("Input a list of student heights: "). split(", ")

sum_of_heights = 0

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

# without sum function
for height in student_heights:
    sum_of_heights += height

average_height = round(sum_of_heights / len(student_heights))

print(f'The average amount of heights is {average_height}')

# with sum function
average_height_test = round(sum(student_heights) / len(student_heights))

print(f'The average amount of heights is {average_height_test}')