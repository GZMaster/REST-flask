student = {
    "name": "John",
    "school": "MIT",
    "grades": (89, 90, 100, 100)
}

def average_grade(data):
    grades = data["grades"]
    return sum(grades) / len(grades)
    
    
def average_grade_all_students(student_list):
    total = 0
    count = 0
    for student in student_list:
        total += average_grade(student)
        count += 1
    return total / count
  
  
print(average_grade_all_students([student]))