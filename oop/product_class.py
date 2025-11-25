class Product:
  def __init__(self, name, price, quantity):
    self.name = name
    self.price = price
    self.quantity = quantity

  def calculate_total_value(self):
    total = self.price * self.quantity
    return f"The total value of {self.name} in stock is {total}"
  
product1 = Product("Sugar", 200, 10)
print(product1.calculate_total_value())


# or make it more flexible for a larger program by: 

# def calculate_total_value(self):
#     return self.price * self.quantity

# product1 = Product("Sugar", 200, 10)
# total = product1.calculate_total_value()
# print(f"The total value of {product1.name} in stock is {total}")
