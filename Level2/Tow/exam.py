from turtle import Turtle, Screen
import random
window= Screen()
sam=Turtle()
sam.hideturtle()
window.title('Badr appGame')
user_choice=window.textinput('Make your bet','''Guess your winner:\n
                             Type a color: Red, BLue or Green?''').lower()
window.setup(width=600, height=400)
colors=['red','blue','green']
y_positions=(-70,0,70)
turtles=[]

for i in range(3):
    turtle_new=Turtle(shape="turtle")
    turtle_new.color(colors[i])
    turtle_new.penup()
    turtle_new.goto(-280,y_positions[i])
    turtle_new.speed('fast')
    turtles.append(turtle_new)



winner=None
while not winner:
    for i in turtles:
        i.forward(random.randint(1, 10))
        if i.xcor()>280:
            winner=i.pencolor()
            break
sam.penup()
sam.goto(0,0)
sam.color('white')
window.bgcolor('pink')
if winner==user_choice:
    sam.write(f'You win! {winner}',align='center',font=('Arial',30,'bold'))
else:
    sam.write(f'You lose!\n {winner} win',align='center',font=('Arial',30,'bold'))
window.exitonclick()