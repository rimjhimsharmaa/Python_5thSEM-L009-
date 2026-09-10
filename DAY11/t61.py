#wap to that asks user  to enter a username and a password.the user shpuld get only 3 attempts.of the credetinals details are entered,display"login succesfull" and stop loop.if all arempts are used,displaybaccount locked.
username = input("Enter username: ") 
password = input("Enter password: ")

for i in range(3):
    if username == "rimjhim" and password == "rimjhim123":
        print("Login Successful")
        break
    else:
        print("invalid cradetals.")
        

