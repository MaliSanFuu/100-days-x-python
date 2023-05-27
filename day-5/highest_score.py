student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

# without for loop
print("with max function")
print(f'The highest value in the list is: {max(student_scores)}')

#with for loop
max = 0

for i in range(len(student_scores)):
    if max < student_scores[i]:
        max = student_scores[i]

print("with for loop")
print(f'The highest value in the list is: {max}')