import math

# squarea= float(input("What is the length of a side of the square in centimeters? "))
# print("The area of the square in square centimeters is: " + str(squarea**2))

# reclength= float(input("What is the length of the rectangle in centimeters? "))
# recwidth= float(input("What is the width of the rectangle? "))
# print("The area of the rectangle in square centimeters is: " + str(reclength*recwidth))

# circle= float(input("What is the radius of the circle in centmeters? "))
# circlearea = (circle**2) * 3.14
# print(f"The area of the circle in square centimeters is: {circlearea:.2f}")

# length= float(input("Please enter a length "))
# print(f"The area of a square is {length**2}")
# print(f"The area of a circle {(length**2)*math.pi: .2f}")
# print(f"The volume of a cube is {length**3}")
# print(f"The volume of a sphere is {(4/3) * math.pi * (length**3): .2f}")

squarea= float(input("What is the length of a side of the square in centimeters? "))
print(f"The area of the square in square centimeters is: {squarea**2}")
print(f"The area of the square in square meters is: {(squarea**2)/100}")

reclength= float(input("What is the length of the rectangle in centimeters? "))
recwidth= float(input("What is the width of the rectangle in centimeters? "))
print(f"The area of the rectangle in square centimeters is: {reclength*recwidth}")
print(f"The area of the rectangle in square meters is: {(reclength*recwidth)/100}")


circle= float(input("What is the radius of the circle in centmeters? "))
circlearea = (circle**2) * math.pi
print(f"The area of the circle in square centimeters is: {circlearea:.2f}")
print(f"The area of the circle in square meters is: {circlearea/100:.2f}")