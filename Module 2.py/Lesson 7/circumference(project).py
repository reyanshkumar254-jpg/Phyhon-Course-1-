def circumference(pi, radius):
    return 2 * pi * radius

radius = int(input("Please enter the radius of your circle: "))
pi = 3.14

result = circumference(pi, radius)
print("Circumference of the circle is:", result)