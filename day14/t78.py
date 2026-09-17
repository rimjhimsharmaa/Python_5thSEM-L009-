#wap to input a list and find the secong largest number in the list
n = int(input("Enter numbers of elements: "))

numbers = []

for i in range(n):
    x = int(input("Enter numbers: "))
    numbers.append(x)

numbers.sort()

print("Second largest number:", numbers[-2])
