"""wap that creates a parking ticket class for calculating the parking fee for 1 vehicle.
the program must: 
    1 ask user to enter the vehicle no and parking duration in hours.the duration may include a fraction,such as 2.5 hours.
    2. calculate the fee using the billable hours:
        - each started hours counts as 1 full hour. for ef 2.1 us billed as 3 hours.
        - charge rs30 per billable hour for the first 2 hours
        - charge rs20 per billable hour after  the first 2 hours
    3.display the vehicle no,actual parking duration and total fee.
    4.if the duration is 0 or negative,display an error message and dont calculate the fee.
 eg:  a vehicle parked for 2.5hr is billed for 3 hpurs the fee is 30+30+20 = 80
 
"""

import math

class ParkingTicket:
    def __init__(self, vehicle_no, hours):
        self.vehicle_no = vehicle_no
        self.hours = hours

    def calculate_fee(self):
        billable_hours = math.ceil(self.hours)

        if billable_hours <= 2:
            fee = billable_hours * 30
        else:
            fee = 2 * 30 + (billable_hours - 2) * 20

        return fee

    def display(self):
        if self.hours <= 0:
            print("Invalid parking duration")
        else:
            fee = self.calculate_fee()
            print("Vehicle No:", self.vehicle_no)
            print("Parking Duration:", self.hours, "hours")
            print("Total Fee: Rs.", fee)


vehicle = input("Enter vehicle number: ")
hours = float(input("Enter parking duration in hours: "))

ticket = ParkingTicket(vehicle, hours)
ticket.display()