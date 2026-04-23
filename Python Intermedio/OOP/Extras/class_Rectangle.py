class Rectangle:
    def __init__(self, width=None, height=None):
        if width is None:
            width = self.get_valid_width()
        if height is None:
            height = self.get_valid_height()
        self.width = width
        self.height = height
    

    def get_valid_width(self):
        while True:
            try:
                width = int(input("Type the width: "))
                if width <= 0:
                    print("The width cannot be negative or zero")
                    continue
                return width
            except ValueError:
                print("Please enter a valid number")
    

    def get_valid_height(self):
        while True:
            try:
                height = int(input("Type the height: "))
                if height <= 0:
                    print("The height cannot be negative or zero")
                    continue
                return height
            except ValueError:
                print("Please enter a valid number")


    def get_area(self):
        self.area = self.width * self.height
        return self.area


    def get_perimeter(self):
        self.perimeter = 2 * (self.width + self.height)
        return self.perimeter


rectangle = Rectangle()
print("\n Calculating the area...")
print(f"Area is: {rectangle.get_area()}")
print("\n Calculating the perimeter...")
print(f"Perimeter is: {rectangle.get_perimeter()}")