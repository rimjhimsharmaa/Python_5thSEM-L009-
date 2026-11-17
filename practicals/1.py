a = int(input("Enter integer: "))
b = float(input("Enter float: "))
c = input("Enter string: ")
d = bool(int(input("Enter 1 or 0: ")))

e = [10, "Apple", 5.5]              # list
f= {"Name": "Rim", "Age": 20}      # dictionary

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))


print("abs:", abs(a))
print("len:", len(c))
print("min:", min(a, 5))
print("round:", round(b))
print("isalnum:", c.isalnum())