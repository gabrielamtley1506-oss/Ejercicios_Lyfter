from abc import ABC , abstractmethod

class Shape:

    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius=1):
        self.radius = radius
        
    def calculate_perimeter(self):
        self.perimeter = (self.radius * 2) * 3.14
        return self.perimeter


    def calculate_area(self):
        self.area = (self.radius ** 2) * 3.14
        return self.area       



class Square(Shape):
    def __init__(self, side_length=2):
        self.side_length = side_length

    def calculate_perimeter(self):
        self.perimeter = self.side_length * 4
        return self.perimeter
    
    
    def calculate_area(self):
        self.area = self.side_length ** 2
        return self.area
        

class Rectangle(Shape):
    def __init__(self, width=2, length=4):
        self.width = width 
        self.length = length

    
    def calculate_perimeter(self):
        self.perimeter = 2 * (self.width + self.length)
        return self.perimeter
    

    def calculate_area(self):
        self.area = self.width * self.length
        return self.area
    

circle1 = Circle()
circle1.radius= 4
print(f"The area and the perimeter of the circle are: \n area:{circle1.calculate_area()} \n perimeter:{circle1.calculate_perimeter()}")

square1 = Square()
square1.side_length = 15
print(f"The area of the square is: {square1.calculate_area()}")
print(f"The perimeter of the square is: {square1.calculate_perimeter()}")

rectangle1 = Rectangle()
rectangle1.width = 5
rectangle1.length = 6
print(f"The perimeter of the rectangle is: {rectangle1.calculate_perimeter()}")
print(f"The area of the rectangle is: {rectangle1.calculate_area()}")

