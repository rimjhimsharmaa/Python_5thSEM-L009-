#wap to input a no and a reverse it using arithemetic  operation 
n = int(input("Enter a number: "))
reverse = 0

while n!=0:
    digit = n % 10
    reverse = reverse * 10 + digit 
    n = n // 10     #remove lst digit from n

print("Reversed number:", reverse)  