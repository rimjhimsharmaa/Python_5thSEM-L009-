#wap to take a word and count the no of vowels a,e,i,o,
word = input("enter word: ")
count = word.count('a')+ word.count('e')+ word.count('i')+ word.count('o')+ word.count('u')

print("Number of vowels in the word:", count)