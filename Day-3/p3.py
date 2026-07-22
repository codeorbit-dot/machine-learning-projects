from math import pi

class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return pi * self.r ** 2


class Rectangle(Shape):
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def area(self):
        return self.l * self.w


n = int(input("Enter shape (1.circle/2.rectangle): "))

if n == 1:
    r = float(input("Enter radius: "))
    shape = Circle(r)

elif n == 2:
    l = float(input("Enter length: "))
    w = float(input("Enter width: "))
    shape = Rectangle(l, w)

else:
    print("Invalid Shape")
    exit()

print(f"Area = {shape.area():.2f}")