# Defining a class
class Smartphone:
    # Contructor
    def __init__(self, brand, model, price, color):
        self.brand = brand  
        self.model = model 
        self.price = price
        self.color = color  

    # Methods
    def get_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Price: ${self.price}")
        print(f"Color: {self.color}")

# Example usage:
my_phone = Smartphone("Apple", "iPhone 14",999.99, "purple")
my_phone.get_info()

# Inheritance
class Smartwatch(Smartphone):
    def __init__(self, brand, model, price, color, battery_life):
        super().__init__(brand, model, price, color)  # Call the constructor of the parent class
        self.battery_life = battery_life  # New attribute for Smartwatch

    def get_info(self):
        super().get_info()  # Call the method from the parent class
        print(f"Battery Life: {self.battery_life} hours")  # New information for Smartwatch

# Example usage:
my_watch = Smartwatch("Apple", "Apple Watch Series 7", 399.99, "black", 18)
my_watch.get_info()


