import random
from turtle import Turtle, Screen

sam =Turtle()
#arrow, turtle, circle, classic, triangle, square, 

sam.color("darkOrange1")
sam.speed("slowest")
def color_shape():
        sam.shape(random.choice(['circle', 'turtle', 'arrow']))
        sam.color(random.choice(['red', 'blue', 'green', 'yellow', 'purple','black']))
        sam.pensize(random.randint(1, 14))
def draw_a_square():
     for _ in range(4):
        color_shape()
        sam.forward(100)
        sam.left(90)

draw_a_square()
 
window =Screen()


window.exitonclick()
