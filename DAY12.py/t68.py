#wap to repeadllety calculate the sum ofof digits of a no until the result becomes a single dogot
n = int(input("enter num"))

while n >= 10:
    total = 0
    while n > 0:
        total += n %10
        n //= 10
    n = total
print("single", n)