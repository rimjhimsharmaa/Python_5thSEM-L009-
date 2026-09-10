#wap to create a simple password validation system
#the program should ask the user to enter a password and until a valid password is entered. a progrm will be cpnsider valid if it has 8 char and a 2 symbol

while True:
    p = input("Enter password: ")

    if len(p) >= 8 and "@" in p:
        print("Valid Password")
        break
    else:
        print("Invalid! Try again")