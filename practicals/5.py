#wap to perform searchinh actitivty using linear abd binary search(use sorted array for binary)

a = [4, 7, 2, 9]
key = int(input("Search for: "))

for i in range(len(a)):
    if a[i] == key:
        print("Found at position", i + 1)
        break
else:
    print("Not found")


    a = [2, 4, 7, 9]
key = int(input("Search for: "))

low, high = 0, len(a) - 1
while low <= high:
    mid = (low + high) // 2
    if a[mid] == key:
        print("Found at position", mid + 1)
        break
    if a[mid] < key:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Not found")