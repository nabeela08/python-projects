student_scores = { 
    "Nabeela" : 82,
    "Suzain" : 88,
    "Zeya" : 85,
    "Abdulla" : 65,
}

student_grades = {}

for student in student_scores:
    scores = student_scores[student]
    if scores > 85:
        student_grades[student]= "Outstading"
    elif scores > 80:
        student_grades[student]= "Excellent"
    elif scores > 70:
        student_grades[student]= "Average"
    else:
        student_grades[student]= "Fail"

print(student_grades)
