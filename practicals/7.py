#wap to create records of n students.store each student record as distionary containing rollno,name,branch,marks.store all recorfs in a list and search for a students uing rollno(rollno must be unqiue)

students = []
n = int(input("Enter number of students: "))

for _ in range(n):
    roll = input("Roll number: ")

    while any(student["roll_no"] == roll for student in students):
        print("Roll number already exists. Enter a unique one.")
        roll = input("Roll number: ")

    student = {
        "roll_no": roll,
        "name": input("Name: "),
        "branch": input("Branch: "),
        "marks": float(input("Marks: "))
    }
    students.append(student)

search_roll = input("\nEnter roll number to search: ")

for student in students:
    if student["roll_no"] == search_roll:
        print("Student record:", student)
        break
else:
    print("Student not found.")