#wap to count to count how many times a particular elements apperars in a list
n = int(input("Enter number of elements: "))    
numbers = []

for i in range(n):
    x = int(input("Enter number: "))
    numbers.append(x)

element = int(input("Enter element to count: "))
count = numbers.count(element)

print("Count of", element, "is:", count)
