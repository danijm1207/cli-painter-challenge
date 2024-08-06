# TODO: Add code here
import matplotlib.pyplot as plt
class Point():
    def __init__(self, x: float, y: float):
        self.x: float = x
        self.y: float = x

class Circle():
    def __init__(self, center: Point, radius: float):
        self.center: Point = center
        self.radius: float = radius


    def area (self):
        pi = 3.1416
        Area = pi * radius**2
        return Area

    def draw ():
        circle = plt.Circle((self.center.x, self.center.y), self.radius, color="r")
        plt.gca().add_patch(circle)
        plt.axis("scaled")
        plt.show()

    def __str__(self):
        Circle
        return f"with center at {self.x}, {self.y} and {self.radius}"

class Triangle():
    def __init__(self, point_1: point,point_2: point, point_3: point):
        self.point_1: point = point_1
        self.point_2: point = point_2
        self.point_3: point = point_3

    def area(self):


