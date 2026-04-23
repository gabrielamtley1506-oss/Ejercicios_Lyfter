class Product:
    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty
    
    def __str__(self):
        return f"Product: {self.name}, Price: ${self.price}, Quantity: {self.qty}"
    
    def get_total_value(self):
        return self.price * self.qty


class Inventory:
    def __init__(self):
        self.products = []
    
    def add_product(self, product):
        self.products.append(product)
    
    def show_all_products(self):
        if not self.products:
            print("Inventory is empty")
            return
        
        print("Inventory")
        for i, product in enumerate(self.products, 1):
            print(f"{i}. {product}")
    
    def calculate_total_inventory_value(self):
        total = sum(product.get_total_value() for product in self.products)
        return total




inventory = Inventory()

p1 = Product("Laptop", 1200, 5)
p2 = Product("Mouse", 25, 10)
p3 = Product("keyboard", 75, 3)


inventory.add_product(p1)
inventory.add_product(p2)
inventory.add_product(p3)


inventory.show_all_products()


print(f"Total value: ${inventory.calculate_total_inventory_value()}")