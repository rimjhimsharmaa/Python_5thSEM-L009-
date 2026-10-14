#instance method: rect area and perimeter
#problem: create a class rectangle to store length and breadth,create an object and use instance to calculate area and perimeter of rectangle.

class Rectangle:
    def area(self):
        print("Area =", 10 * 5)

    def perimeter(self):
        print("Perimeter =", 2 * (10 + 5))

r = Rectangle()
r.area()
r.perimeter()