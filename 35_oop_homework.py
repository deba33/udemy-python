class Line():

    def __init__(self, coor1=[0, 0], coor2=[1, 1]):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):

        x1, y1 = self.coor1
        x2, y2 = self.coor2
        dist = (((x2-x1)**2)+((y2-y1)**2))**0.5
        return dist

    def slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        slp = (y2-y1)/(x2-x1)
        return slp


c1 = [2, 5]
c2 = [4, 9]

li = Line(c1, c2)

print(li.distance())

print(li.slope())
