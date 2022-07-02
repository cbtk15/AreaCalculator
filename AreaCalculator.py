"""
Area Calculator in Python 2

Calculator that can compute the area of a circle or a triangle.

This program:
- Prompts the user to select a shape,
- Calculate the area of that shape,
- Print the area of that shape to User.

"""
valid = False

print "Area Calculator online"

while valid == False:
  valid = True
  option = raw_input("Enter C for Circle and T for Triagle: ")
  if option == "C" or option == "c":
    circle_radius = float(raw_input("Enter the circle radius: "))
    circle_area = 3.14159 * circle_radius**2
    print "A circle with the radius of %d has an area of %d." % (circle_radius, circle_area)
  elif option == "T" or option == "t":
    base = float(raw_input("Enter the triangle height: "))
    height = float(raw_input("Enter the triangle base: "))
    area = 0.5 * base * height
    print "A triangle with the height of %d and a base of %d, has an area of %d." % (height, base, area)
  else:
    print "Shape Invalid: Please enter a valid shape."
    valid = False
  

print "calculation ended."



