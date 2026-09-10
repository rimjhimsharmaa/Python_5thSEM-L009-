#wap to input four no and find the greatest no amoung them
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

if a >= b and a >= c and a >= d:
    print("Greatest number =", a)
elif b >= c and b >= d:
    print("Greatest number =", b)
elif c >= d:
    print("Greatest number =", c)
else:
    print("Greatest number =", d)