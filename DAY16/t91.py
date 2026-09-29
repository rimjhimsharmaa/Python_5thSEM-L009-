#WAP TO STORE MULTIPLE STUDENTS RECORDS A LIST OF TUPLES.EACH TUPLE SHOULD CONTAIN NAME,ROLL NO AND MARKS.DISPLAY STUDENTS WHO STORED ABOVE 75

n = int(input("Enter number of students: "))

students = []

for i in range(n):
    print("\nEnter details of student", i + 1)

    name = input("Enter name: ")
    roll = int(input("Enter roll number: "))
    marks = float(input("Enter marks: "))

    student = (name, roll, marks)
    students.append(student)

print("\nStudents who scored above 75:")

for student in students:
    if student[2] > 75:
        print("Name:", student[0])
        print("Roll Number:", student[1])
        print("Marks:", student[2])
        print()