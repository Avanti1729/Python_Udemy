class Circle():
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius
        self.area = self.radius * self.radius * Circle.pi

    def get_Circumference(self):
        return self.radius * Circle.pi * 2


my_circle = Circle(30)
print(my_circle.radius)
print(my_circle.pi)
print(my_circle.area)
print(my_circle.get_Circumference())

