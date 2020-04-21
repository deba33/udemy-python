class Line:

    def __init__(self, coor1=(1, 0), coor2=(0, 1)):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2

        dist = (((x2-x1)**2)+((y2-y1)**2))**(0.5)

        return f"Distance between {self.coor1} and {self.coor2} is {dist}"

    def slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2

        slp = (y2-y1)/(x2-x1)

        return f"Slope between {self.coor1} and {self.coor2} is {slp}"


coordinate1 = (3, 2)
coordinate2 = (8, 10)

li = Line(coordinate1, coordinate2)

print(li.distance())
print(li.slope())
