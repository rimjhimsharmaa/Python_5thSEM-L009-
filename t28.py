#wap to take a students full name and display: total number of characters. first character, last character, name in uppercase.
name = input("Enter the student's full name: ")
print(f"Total number of characters: {len(name)}")
print(f"First character: {name[0]}")
print(f"Last character: {name[-1]}")
print(f"Name in uppercase: {name.upper()}")