f = open("MyFile.txt", "r")

text = f.read()

words = text.split()

unique_words = set(words)

sorted_words = sorted(unique_words)

print("Unique words in alphabetical order:")

for word in sorted_words:
    print(word)

f.close()