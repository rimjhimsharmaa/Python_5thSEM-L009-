#wap to input 2 lists and create a third list conanting commen elements


list1 = [1, 2, 4, 3]
list2 = [2, 3, 4, 5]

common = []

for x in list1:
    if x in list2:
        common.append(x)

print("Commmon elements:",common)