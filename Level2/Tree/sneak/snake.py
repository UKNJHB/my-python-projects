from turtle import Turtle

class Snake():

    def __init__(self):
        self.turtles=[]
        self.positions=[(-40,0),(-20,0),(0,0)]
        self.creat_sneak()
        self.head=self.turtles[-1]
    def creat_sneak(self):
        for i in range(len(self.positions)):
            new_sneak=Turtle('square')
            new_sneak.color('white')
            new_sneak.penup()
            new_sneak.goto(self.positions[i])
            self.turtles.append(new_sneak)
 
    def move(self):
        for i in range(len(self.turtles)-1):
            self.turtles[i].goto(self.turtles[i+1].pos())
        self.head.forward(20)

    def extend(self):
            new_segment= Turtle("square")
            new_segment.color('white')
            new_segment.penup()
            new_segment.goto(self.turtles[0].pos())
            self.turtles.insert(0, new_segment) 


    def up(self):
        self.head.setheading(90)
        print('up')
    def down(self):
        self.head.setheading(270)
    def left(self):
        self.head.setheading(180)
    def right(self):
        self.head.setheading(0)
    
