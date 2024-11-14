
grade_list = []
passed_subject = []


while True:
    grade = input("Enter your grade (Type 'Done/done' to exit): ")
    
    if grade.lower() == 'done':
        break
    if not grade.isdigit() or int(grade) <= 39 or int(grade) >= 101:
        print("Invalid input. Please enter grade between 40 and 100 next time.")
    else:
        grade = int(grade)
        grade_list.append(grade)
        if grade >= 75:
            passed_subject.append(grade)
        print("Your grade is", grade)
        
if grade_list:
    grade_average = sum(grade_list) / len(grade_list) if grade_list else 0
    passing_percentage = (len(passed_subject) / len(grade_list)) * 100
    
    print(f"The Average grade is {grade_average:.2f}")
    print(f"The Passing percentage is {passing_percentage:.2f}%")
    print(f"Number of students who passed: {len(passed_subject)}")
    print(f"The Grades: {grade_list}")
else:
    print("There have been no grade entered.")
