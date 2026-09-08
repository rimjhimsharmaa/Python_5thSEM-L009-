#   wp to take a passsword and check whether it contains @ and has at least 8 char 
password = input("enter password")
print(" password ", "@" in password and len(password) >= 8)