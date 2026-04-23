class Circle:
    def __init__(self, radius=3):
        self.radius = radius
        
    def get_area(self):
        self.area = 3.14 * (self.radius**2)
        return self.area
    

circle_1=Circle()
print(f"The area for circle 1 is: {circle_1.get_area()}")

circle_2=Circle()
circle_2.radius=7
print(f"The area for circle 2 is: {circle_2.get_area()}")

circle_3=Circle()
circle_3.radius=4
print(f"The area for circle 3 is: {circle_3.get_area()}")