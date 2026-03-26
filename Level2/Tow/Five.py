from turtle import Turtle, Screen
import random
window= Screen()
sam= Turtle()
def color_shape():
        sam.shape(random.choice(['circle', 'turtle', 'arrow']))
        sam.color(random.choice(['red', 'blue', 'green', 'yellow', 'purple','black']))
        sam.pensize(random.randint(1, 14))
def draw_a_square():
        color_shape()
        for _ in range(4):
            sam.forward(100)
            sam.left(90)
def draw_circle():
        color_shape()
        sam.circle(50,360)

def draw_triangle():
        color_shape()
        for _ in range(3):
               sam.forward(100)
               sam.left(120)

sam.hideturtle()

while True:
  user_choice= window.textinput("لحظة من فضلك",'ما الذي تريد أن ترسمه؟ دائرة, مربع, مثلث')
  if user_choice=='circle'or user_choice=='دائرة':
       draw_circle()
  elif user_choice=="square"or user_choice=='مربع':
         draw_a_square()
  elif user_choice=="triangle"or user_choice=='مثلث':
            draw_triangle()
  elif user_choice=="exit"or user_choice=='خروج':
        
        break
  

  else:
        continue
sam.clear()
sam.penup()
window.bgcolor('AliceBlue')
sam.color('Black')
sam.write("Press any key to exit", align="center", font=("Arial", 30, "bold"))
sam.goto(0,-30)
sam.color("azure3")
sam.write("اضغط على أي مكان للخروج",align='center', font=("Arial", 20, "normal"))
window.exitonclick()