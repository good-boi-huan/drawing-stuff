import turtle

def circle(radius, color):
  z.circle(radius)
  z.fillcolor(color)

def star(length, color):
  for i in range(5):
    z.forward(length)
    z.right(144)
    z.fillcolor(color)

def polygon(length, sides, color):
  angle = 360/sides
  z.forward(length)
  z.right(angle)
  z.fillcolor(color)

play = True
z = turtle.Turtle()
z.penup()
z.sety(100)
z.pendown()

while play == True:
  shape = input("Which shape would you like to draw?\nCircle\nStar\nPolygon\n")
  if shape.lower == "circle":
    radius = int(input("What is the radius of your circle? "))
    color = input("What color is your circle? ")
    circle(radius, color)
  elif shape.lower == "star":
    length = int(input("How long do you want the sides? "))
    color = input("What color is your star? ")
    star(length, color)
  elif shape.lower == "polygon":
    sides = input("How many sides does your polygon have? ")
    length = int(input("How long are the sides? "))
    color = input("What color is your polygon? ")
    polygon(length, sides, color)
  play_again = input("Do you want to play again (y/n)? ")
  if play_again == "n":
    play = False