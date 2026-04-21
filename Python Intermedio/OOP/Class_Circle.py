class Circle:
    radius=3
        
    def get_area(self):
        area=3.14 * (self.radius**2)
        print(f"The area is {area}")
        return area
    

circle_1=Circle()
circle_1.get_area()

circle_2=Circle()
circle_2.radius=7
circle_2.get_area()

circle_3=Circle()
circle_3.radius=4
circle_3.get_area()
