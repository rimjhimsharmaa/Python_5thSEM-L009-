s = "Welcome to Python world"

# Count alphabets
count = 0

for ch in s:
    if ch.isalpha():
        count += 1

print("Alphabets:", count)
print("Characters:", s[0:15])
print("Alphanumeric:", s.isalnum())