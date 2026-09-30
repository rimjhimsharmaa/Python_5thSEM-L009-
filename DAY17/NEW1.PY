"""Write a Python program to allocate seats to a group in a single row of a cinema hall. First, input the total number of seats n. Then enter the status of each seat:
 0 means the seat is available.
 1 means the seat is already booked.
Next, input the number of people in the group. Find the first consecutive block of available seats that can accommodate the entire group.
 If available, book those seats by changing their status from 0 to 1, display the allocated seat numbers as a tuple, and display the updated list of seat statuses
 .
# If no consecutive block is available, display "Consecutive seats not available" and print the original seat list without any changes."""

"""Conditions: Seat numbering starts form 1 . 2 the group size must be atleast 1 and cant exceed n.   3  
 All group members must be allotted seats together in consecutive order.
 If more than one suitable block is available, allocate the first block from the left.
    Input seat status must be either 0 or 1."""

n = int(input("Enter number of seats: "))

seats = []
for i in range(n):
    x = int(input("Enter seat status (0/1): "))
    seats.append(x)

group = int(input("Enter number of people: "))

found = False
