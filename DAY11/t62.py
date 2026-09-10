#wap to input a no and check whther it is prime or or not

num = int(input("enter a number: "))
if num > 1 and num % 2 == 1:
    print("its prime")
else:
    print("not prime")