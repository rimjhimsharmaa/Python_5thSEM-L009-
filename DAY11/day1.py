
print("hi rim")     #hie  i am rimmmm


# write a py program which to print the contents of a directorty using the os module 
print("hi")          # hey its py

# write a py program which prints the contents of a directory using os module
import os

result = os.listdir()        # () return a list of files and folders
print(result)

# 2 print the path
print(os.getcwd())

# 3 use os module to create a folder in d
#os.mkdir("ok")

# 4 check whether a folder is already made
print(os.path.exists("rim"))
print(os.path.exists("1111111111"))

# rename
os.rename("day1.py", "day1a2.py")

# isfile check if a file exists
print(os.path.isfile("day3.py"))
print(os.path.isdir("ok"))

# remove
print(os.remove("ok"))