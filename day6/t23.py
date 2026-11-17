#wap to detect double spaces in a string
string = input("Enter a string: ")
if "  " in string:
    print("Double spaces found!")
else:
    print("No double spaces found.")