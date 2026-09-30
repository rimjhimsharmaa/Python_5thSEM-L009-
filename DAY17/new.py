"""wap to input a students marks in n consecutive tests and store them in a list.find the longest consective sequence in which each  mark is stricly greater than previous mark.
display the sequence ,its lenghth and its starting and ending test no as a tuple.if multiple seq have same max lenghth,display the  first one.
markks"""

"""marks [50,60,68,62,65,70,78,74]
longest improving seq: [62,65,70,78]
NO OF TESTS : 4
TEST RANGE: (4,7 )"""

"""CONDITIONS: ACCEPTATLEAST ONE TEST,EQUAL MARKS BREAK THE IMPROVING SEQEUNCE,TEST NO BEGINS AT 1.DONT SORT THE lIST BCOZ ORIGINAL LIST ORDER MATTERS."""




n = int(input("Enter number of test: "))
marks = []
for i in range(n):
    marks.append(int(input("enter Marks:")))
start = 0
best_start = 0
best_length = 1

for i in range(1,n):
    if marks[i]<= marks[i-1]:
        start = 1
    length = i - start + 1

    if length > best_length:
        best_start = start
        best_length = length

sequence = marks[best_start:best_start + best_length]
test_range = (best_start + 1,best_start + best_length)

print("Longest improving sequence:", sequence)
print("Numbers of tests:", best_length)
print("Test range:", test_range)


















