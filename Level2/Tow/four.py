from turtle import Turtle, Screen

window= Screen()
window.setup(width=1000, height=1000)
window.bgcolor("black")


sam= Turtle()
sam.shape("turtle")
sam.color("white")
sam.speed("fastest")
sam.pensize(3)
def draw_circle():
    sam.penup()
    sam.goto(-300,-300)
    sam.pendown()
    for _ in range(10):
     sam.circle(50)
     sam.left(360/10)

def draw_triangle():
    sam.penup()
    sam.goto(300,300)
    sam.pendown()
    for _ in range(10):
     for _ in range(3):
      sam.forward(100)
      sam.left(120)
     sam.left(360/10)
     
def draw_square():
   sam.penup()
   sam.goto(0,0)
   sam.pendown()
   for _ in range(10):
      for _ in range(4):
       sam.forward(100)
       sam.left(90)

      sam.left(360/10)
draw_circle()
draw_triangle()
draw_square()
      


window.exitonclick()