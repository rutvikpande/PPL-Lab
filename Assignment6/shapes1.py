import turtle

screen=turtle.getscreen()
t=turtle.Turtle()

class shapes:
    def __init__(self,sides=0,length=0):
        self.sides=sides
        self.length=length

class polygon(shapes):
    def info(self):
        print("Polygon is a plane figure with at least three straight sides and angles.")

class square(polygon):
    def show(self):
        for i in range(4):
            t.forward(self.length)
            t.right(90)

class pentagon(polygon):
    def show(self):
        for i in range(5):
            t.forward(self.length)
            t.right(72)

class hexagon(polygon):
    def show(self):
        for i in range(6):
            t.forward(self.length)
            t.right(60)

class octagon(polygon):
    def show(self):
        for i in range(8):
            t.forward(self.length)
            t.right(45)

class triangle(polygon):
    def show(self):
        t.forward(self.length)
        t.left(120)
        t.forward(self.length)
        t.left(120)
        t.forward(self.length)

squ1=square(4,100)
squ1.show()

pent1=pentagon(5,100)
pent1.show()

hex1=hexagon(6,100)
hex1.show()

oct1=octagon(8,100)
oct1.show()

tri1=triangle(3,100)
tri1.show()


