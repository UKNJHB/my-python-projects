from turtle import Turtle, Screen
window=Screen()
window.setup(width=800,height=800)
window.bgcolor('black')
positions=[(-40,0),(-20,0),(0,0)]
turtles=[]


for i in range(3):
    new_turtle=Turtle("square")
    new_turtle.color('white')
    new_turtle.penup()
    new_turtle.speed("slow")
    new_turtle.goto(positions[i])
    turtles.append(new_turtle)

#move
for i in range(5):
    turtles[2].forward(100)
    turtles[2].left(90)
    turtles[1].goto(turtles[2].pos())
    turtles[0].goto(turtles[1].pos())   
      
         
window.exitonclick()