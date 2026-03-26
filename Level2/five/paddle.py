from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):#2 things will take
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.goto(position)
        self.shapesize(stretch_wid=5,stretch_len=1)#make paddle longer
    def go_up(self):
        self.goto(self.xcor(),self.ycor()+40)
    def go_down(self):
        self.goto(self.xcor(),self.ycor()-40)