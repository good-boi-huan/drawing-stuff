import turtle

def circle(radius, color):
  z.color(color)
  z.begin_fill()
  z.circle(radius)
  z.end_fill()
  

def star(length, color):
  z.color(color)
  z.begin_fill()
  for i in range(5):
    z.forward(length)
    z.right(144)
    z.fillcolor(color)
  z.end_fill()

def polygon(length, sides, color):
  angle = 360/sides
  z.color(color)
  z.begin_fill()
  for i in range(0, sides):
    z.forward(length)
    z.right(angle)
    z.fillcolor(color)
  z.end_fill()

play = True
z = turtle.Turtle()


while play == True:
  z.clear()
  shape = input("Which shape would you like to draw?\nCircle\nStar\nPolygon\n")
  if shape.lower() == "circle":
    radius = int(input("What is the radius of your circle? "))
    color = input("What color is your circle? ")
    circle(radius, color)
  elif shape.lower() == "star":
    length = int(input("How long do you want the sides? "))
    color = input("What color is your star? ")
    star(length, color)
  elif shape.lower() == "polygon":
    sides = int(input("How many sides does your polygon have? "))
    length = int(input("How long are the sides? "))
    color = input("What color is your polygon? ")
    polygon(length, sides, color)
  play_again = input("Do you want to play again (y/n)? ")
  if play_again == "n":
    play = False