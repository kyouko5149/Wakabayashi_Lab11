
grade_list = []
passed = []

while True:
    grade = input("Enter your grade (Type 'Done/done' to exit): ")
    if grade.lower() == 'done':
        break
    else:
        grade = int(grade)
        grade_list.append(grade)
        if grade >= 75:
            passed.append(grade)
            print("Your grade is", grade)
if grade_list:
    grade_average = sum(grade_list) / len(grade_list)
    passing_percentage = len(passed) / len(grade_list) * 100
    passed_percentage = int(passing_percentage)
    print(f"Your Average grade is {grade_average:.2f}")
    print(f"Your Passing percentage is {passing_percentage:.2f}%")
    print(f"Your Grades: {grade_list}")
else:
    print("There have been no grade entered.")