#wap to calculate si and total amount using prinical,rate and time entered by the user
 
p = float(input("e pa ")) 
r = float(input("e roi ")) 
t = float(input("e time ")) 

s_i = (p*r*t)/100
total = p*s_i

print("si",s_i)
print("total ama ", total)