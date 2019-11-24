class Circle():

    # CLASS  OBJECT ATTRIBUTE
    pi = 22/7

    def __init__(self, radius=1):
        self.radius = radius
        self.circumference = self.radius*self.pi*2
        self.area = self.pi*(self.radius**2)

    # METHOD

    def get_circumference(self):
        return ("Circumference of the Circle is " + str(self.circumference)+" m")

    def get_Area(self):
        return ("Area of the Circle is " + str(self.area) + " m X m")


radius = int(input("Please enter Radious of the circle: "))
my_circle = Circle(radius)

print(my_circle.get_circumference() + "\n" + my_circle.get_Area())
