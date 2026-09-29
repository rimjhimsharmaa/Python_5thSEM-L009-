#wap to show that tuple values cant be changed directly.convert tuple into list,update it and convert back into tuple.
t = (1, 2, 3, 4, 5)
print("Original tuple:", t)

l = list(t)                   
print("Converted list:", l)


l[2] = 10
print("Updated list:", l)

t = tuple(l)
print("Converted back to tuple:", t)