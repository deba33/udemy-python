class Cylinder:

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        vol = 3.14*(self.radius**2)*self.height
        return f"Volume of cylinder is {vol}"

    def surface_area(self):
        s_area = (2*3.14*self.radius)*(self.height+self.radius)
        return f"Surface Area of cylinder is {s_area}"


c = Cylinder(2, 3)

print(c.volume())
print(c.surface_area())
