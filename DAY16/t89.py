#wap to check whether a given value is present in a tuple.if presesnt display its position
t = (1, 2, 3, 4, 5)
value = int(input("Enter a value to check: "))

if value in t:
    position = t.index(value)
    print(f"The value {value} is present at position {position}.")
else:
    print(f"The value {value} is not present in the tuple.")