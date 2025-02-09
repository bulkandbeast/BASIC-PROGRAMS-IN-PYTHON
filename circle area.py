#area of a circle
radius=int(input("enter the radius"))
def area_of_circle(radius):
    import math
    return math.pi * radius ** 2

print("Area of Circle with given radius:", area_of_circle(radius))
