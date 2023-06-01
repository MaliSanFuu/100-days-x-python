student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,    
}

# Iterate over each student's score and print it
for student in student_scores:
    print(f'The student {student} has the score {student_scores[student]}')

print("- - - - - - - - - - - ")
student_grades = {}

# Iterate over each student's score
for student in student_scores:
    # Assign grades based on the score
    if student_scores[student] >= 91:
        student_grades[student] = "Outstanding"  
    elif student_scores[student] >= 81:
        student_grades[student] = "Exceeds Expectations"  
    elif student_scores[student] >= 71:
        student_grades[student] = "Acceptable"  
    else:
        student_grades[student] = "Fail"  

# Print the grades for each student
for student in student_grades:
    print(f'The student {student} has the score {student_grades[student]}') 
