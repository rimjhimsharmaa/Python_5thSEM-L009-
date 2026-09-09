#wap to calculate the final bill amount after applying discount. THE PROGRA, SH0ULD TAKE TO TOTAKL BILL AS INPUT FROM THE USER AND APPLY DISCOUNT AT TO THE RULES AFTER CALCULATING DISCOUNT .THE PROHRAM SHOULD DISPLAY the discount amount and the final payable by the customer . above 5000 20 percemt and 
#3000 to 5000 10 percent

#below 3000 5 percent

bill = float(input("Enter total bill amount: "))

if bill > 5000:
    discount = bill * 20 / 100
elif bill >= 3000:
    discount = bill * 10 / 100
else:
    discount = bill * 5 / 100

final_bill = bill - discount

print("Discount amount =", discount)
print("Final payable amount =", final_bill)



