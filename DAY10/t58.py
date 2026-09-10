#wap to input marks of 5 students.for each student the program should check whther the marks are valid or invalid. marks are valid id b/w 0 and 100 if the marks are invalid the program should display"invalid skipped" and move to the nedxt student without printing thpse marks

for i in range(5):
    marks = int(input("Enter marks: "))

    if marks < 0 or marks > 100:
        print("Invalid skipped")
        continue

    print("Marks =", marks)

    