#wap to rotate a list one position to the right
n = int(input("Enter number of elements: "))

numbers = []

for i in range(n):
    x = int(input("Enter number: "))
    numbers.append(x)

last = numbers[-1]

for i in range(n - 1, 0, -1):
    numbers[i] = numbers[i - 1]

numbers[0] = last

print("Rotated list:", numbers)