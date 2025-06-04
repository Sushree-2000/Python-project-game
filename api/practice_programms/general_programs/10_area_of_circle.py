# 10 - How to find Area of a Circle in Python
import math
class Areas():
    def __init__(self, shape):
        shape = str(input("Give the shape to find out the area for: "))
        # print("Give all required parameters to find the area of a "+shape)
        if(shape.lower() == 'circle'):
            radius = float(input("Provide the radius of the Circle: "))
            self.circArea(radius)
        if(shape.lower() == 'triangle'):
            self.radius = float(input("Provide the radius of the Circle: "))
        if(shape.lower() == 'square'):
            self.radius = float(input("Provide the radius of the Circle: "))
        if(shape.lower() == 'rectangle'):
            self.radius = float(input("Provide the radius of the Circle: "))
        if(shape.lower() == 'trapisium'):
            self.radius = float(input("Provide the radius of the Circle: "))
    def circArea(self, radius):
        area_circ = math.pi*(radius**2)
        print(f"Area of the circle having radius {radius} = {area_circ}")
    def triangleArea(self, side1, side2, side3):
        # p = 3*side  #perimeter
        p = side1*side2*side3  #perimeter
        area = (p*(p-side1)*(p-side2)*(p-side3))**2
        print(f"Area of the circle having sides {side1},{side2},{side3} = {area}")
    def squareArea(self, radius):
        area_circ = math.pi*(radius**2)
        print(f"Area of the circle having radius {radius} = {area_circ}")

area_obj = Areas('circle')
# area_obj.circArea(area_obj.radius)
