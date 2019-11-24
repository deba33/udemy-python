class Cylinder():

    pi = 22/7

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        volume = (self.pi) * (self.radius**2) * (self.height)
        return volume

    def surface_area(self):
        s_area = (2*self.pi*self.radius)*(self.height+self.radius)
        return s_area

c = Cylinder(2, 3)

print(c.volume())
print(c.surface_area())