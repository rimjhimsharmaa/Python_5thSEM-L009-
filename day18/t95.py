#create a product class with product name and price and quantity.add an instance method to calcualte total cost.take these values from user 
#and display product name and total cost.
class Product:
    def _init_(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total(self):
        return self.price * self.quantity
name = input("Enter product name: ")
price = float(input("Enter product price: "))
quantity = int(input("Enter product quantity: "))
product1 = Product(name, price, quantity)
print(f"Product Name: {product1.name}")
print(f"Total Cost: {product1.calculate_total()}")