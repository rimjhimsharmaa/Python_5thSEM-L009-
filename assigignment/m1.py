# ==========================================
# Artisan Coffee Roastery Batch Tracker
# Milestone 1 - Single Batch Calculator
# Author: Alex (Updated this script after breaking it yesterday, lol)
# ==========================================

import sys # sometimes we need this, keeping it here just in case

print("Welcome to the Coffee Roastery Tracker v1.0")

# TODO: Maybe wrap this in a loop later so we don't have to restart every time?
# getting inputs from user... hopefully they type numbers where they are supposed to

batch_id = input("Enter Batch ID: ")
origin = input("Enter Coffee Origin: ")

# wait, let me make sure these convert properly. 
# wrapping in float/int can throw an error if user types letters, 
# but whatever, we'll deal with error handling next week maybe.
green_weight = float(input("Enter Green Bean Weight (kg): "))
loss_percent = float(input("Enter Roast Loss (%): "))
roast_time = int(input("Enter Roasting Time (minutes): "))
price_per_kg = float(input("Enter Selling Price per kg (Rs.): "))

# Just checking types as requested by the assignment brief
print("\n[DEBUG] --- DATA TYPES CHECK ---")
print("Green Weight variable type is:", type(green_weight))
print("Roast Loss variable type is:", type(loss_percent))
# print("Just testing if everything runs fine up to here...")

# Math calculations for the roast batch
# Formula given: roasted weight = green weight - (green weight x loss% / 100)
weight_lost = green_weight * (loss_percent / 100)
roasted_weight = green_weight - weight_lost

# calculating yield percentage... make sure not to divide by zero!
if green_weight > 0:
    yield_percent = (roasted_weight / green_weight) * 100
else:
    yield_percent = 0.0

# Estimated total value of the batch after roasting
batch_value = roasted_weight * price_per_kg

# Figure out hours and mins using floor division and modulus
hours_took = roast_time // 60
mins_took = roast_time % 60

# Making a short batch code using string slicing operations
# Note: if batch_id is too short this might break, let's just hope users follow instructions
if len(batch_id) >= 5:
    short_code = batch_id[:2] + batch_id[-3:]
else:
    short_code = batch_id # fallback if it's a weird short ID

# Printing out the final report nicely formatted
print("\n")
print("=========================================")
print("     COFFEE ROASTING BATCH REPORT        ")
print("=========================================")
print("Batch ID entered:   ", batch_id)
print("Coffee Origin:      ", origin)
print("Generated Code:     ", short_code)
print("-----------------------------------------")
print("Green Bean Weight:  ", green_weight, "kg")
print("Roast Loss Target:  ", loss_percent, "%")
print("Actual Weight Lost: ", round(weight_lost, 2), "kg")
print("Final Roasted Wt:   ", round(roasted_weight, 2), "kg")
print("Roasting Yield:     ", round(yield_percent, 2), "%")
print("-----------------------------------------")
print("Total Roast Time:   ", hours_took, "hours and", mins_took, "minutes")
print("Price per kg:       Rs.", price_per_kg)
print("Est. Batch Value:   Rs.", round(batch_value, 2))
print("=========================================")

# End of script for milestone 1. Don't forget to push to github later!