#create a database using lists and rtuples.each student record must contai  rollno,name ,branch, and cggpa.store each record as tuple in

students = []
n = int(input("Number of students: "))

for _ in range(n):
    roll = input("Roll no: ")
    while any(s[0] == roll for s in students):
        print("Roll number already used.")
        roll = input("Enter a unique roll no: ")

    students.append((roll, input("Name: "), input("Branch: "),
                     float(input("CGPA: "))))

print("\nRecords:")
for student in students:
    print(student)

key = input("\nSearch roll no: ")
for student in students:
    if student[0] == key:
        print("Found:", student)
        break
else:
    print("Not found")