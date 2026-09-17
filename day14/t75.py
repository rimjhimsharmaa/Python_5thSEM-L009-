#wap a program to print hallow square using stars
n = int(input("Enter rows: "))

for i in range(n):           #rows
    for j in range(n):         #col
        if i == 0 or i == n-1 or j == 0 or j == n-1:      
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

