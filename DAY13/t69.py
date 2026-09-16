#wap to print the following pattern for n row!
n = int(input("Enter rows: "))  #take how many rows we want.

for i in range(1, n + 1):     #decide th rn
    for j in range(1, i + 1):    # print
        print(j, end="")
    print()


#