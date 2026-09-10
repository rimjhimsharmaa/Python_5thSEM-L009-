#wap to take 2 no using ip and find gcd using loop
import math
a = int(input("enter num"))
b = int(input("enter  sec num"))

num1,num2 = a,b

while b!=0:
    remainer = a%b
    a = b
    b= remainer

print(f"the gcd of {num1}and{num2}")

