from turtle import Turtle, Screen
import random

window= Screen()

window.setup(width=800, height=800)
window.bgcolor("black")
sam = Turtle()
sam.shape("turtle")
sam.color("white")
sam.speed("fast")
sam.pensize(2)

tom = Turtle()
tom.shape("square")
tom.color("orange")
tom.speed("fastest")
tom.pensize(5)

my_angles=(0, 90, 180, 270)
my_distance = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
loop_count=(5, 10, 15, 20)#tuple #immutable
def draw_random(turtle_name):
    for _ in range(random.choice(loop_count)):
        turtle_name.forward(random.choice(my_distance))
        turtle_name.left(random.choice(my_angles))
for _ in range(20):
    tom.circle(100)
    tom.left(360/20)
window.exitonclick()