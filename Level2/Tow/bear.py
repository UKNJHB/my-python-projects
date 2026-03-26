from turtle import Turtle, Screen

sam = Turtle()
sam.shape("turtle")
sam.color("red")
for i in range(4):
 sam.forward(100)
 sam.left(90)
 sam.forward(100)
 sam.left(90)
 sam.forward(100)
 sam.left(90)
 sam.forward(100)
sam.left(90)
sam.forward(100)
sam.left(90)
sam.circle(50, 180)
sam.circle(-50, 180)
sam.forward(100)
sam.right(135)
sam.forward(300)
window= Screen()




window.exitonclick()
