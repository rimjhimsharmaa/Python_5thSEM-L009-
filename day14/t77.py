#wap to input marks of 10 students.store valid marks between 0 to 100 in a list skip invalid marks

marks = []

for i in range(10):
    m = int(input("Enter marks: "))

    if m >= 0 and m <= 100:
        marks.append(m)

print("Valid marks:", marks)