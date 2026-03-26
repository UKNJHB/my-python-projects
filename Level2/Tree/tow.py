from turtle import Turtle, Screen
import random
import time
window=Screen()
window.setup(width=800,height=800)
window.bgcolor('black')
positions=[(-40,0),(-20,0),(0,0),(20,0),(40,0),(60,0),(80,0)]
turtles=[]
angles=[90,0,0,0]
window.tracer(0)
for i in range(len(positions)):
    new_turtle=Turtle("square")
    new_turtle.color('white')
    new_turtle.penup()
    new_turtle.speed("slow")
    new_turtle.goto(positions[i])
    turtles.append(new_turtle)
game_on=True
while game_on:
    for i in range(len(turtles)-1):
        turtles[i].goto(turtles[i+1].pos())
    turtles[-1].forward(20)
    
    turtles[-1].left(random.choice(angles))
    window.update() 
    time.sleep(0.1)   
window.exitonclick()