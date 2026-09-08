#wap to take a 10 digit mobile number and display only the last 4 digits. replace the first 6 digits with ******
mobile_no = input("Enter a 10 digit mobile number: ")
print("Last 4 digits:", mobile_no[-4:])
print("Masked number:", "*" * 6 + mobile_no[-4:])