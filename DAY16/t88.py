#wap to store repeated values in a tuple and count how many times a given value appears
t = (1, 2, 3, 2, 4, 2, 5)
print("Original tuple:", t)

value = int(input("Enter a value to count: "))
count = t.count(value)
print(f"The value {value} appears {count} times in the tuple.")