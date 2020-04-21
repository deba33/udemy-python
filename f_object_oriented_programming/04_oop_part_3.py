class Circle():

    """ provide a radius to calculate the circumference and area of a Circle

    Ex:
        var=Circle(radius=1)

        print(var.calc_circumference)
        print(var.calc_area) """

    # class object attribute
    pi = 3.14

    def __init__(self, radius=1):

        self.radius = radius

    # methods
    def calc_circumference(self):
        return 2 * self.pi * self.radius

    def calc_area(self):
        return self.pi * (self.radius ** 2)


cir = Circle(10)

print(cir.radius, cir.calc_circumference(), cir.calc_area())
