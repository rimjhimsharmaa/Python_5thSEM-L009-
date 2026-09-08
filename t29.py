#wap to take a student name and roll no, then generate a username using the first 3 characters of the name and last 2 digits of the roll no.
name = input("Enter the student's name: ")
roll_no = input("Enter the student's roll number: ")
username = name[:3] + roll_no[-2:]
print("Generated username:", username)