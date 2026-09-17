#wap to input a list and create a new list with only unqiue elemets

n = int(input("Enter number of elements: "))

numbers = []

for i in range(n):
    x = int(input("Enter number: "))
    numbers.append(x)

unique = []

for x in numbers:
    if x not in unique:
        unique.append(x)

print("Unique elements:", unique)