from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboardr
import time

window=Screen()
window.setup(width=800,height=800)
window.bgcolor('black')
window.title('Sneak Game')

window.tracer(0)
snake=Snake()
food=Food()
score=Scoreboardr()
def stop_game():
        global game_on
        game_on=False

                
game_on=True
while game_on:
    snake.move()
    window.update()
    time.sleep(0.1)
    window.listen()
    window.onkey(snake.up,"Up")
    window.onkey(snake.down,'Down')
    window.onkey(snake.left,'Left')
    window.onkey(snake.right,'Right')
    window.onkey(stop_game,'space')
    if snake.head.distance(food)<15:
          food.appear()
          snake.extend()
          score.increase_score()
    if snake.head.xcor()>390 or snake.head.xcor()<-390 or snake.head.ycor()>390 or snake.head.ycor()<-390:
          game_on=False
          score.game_over()
      
    for segment in snake.turtles[:-1]:
          if snake.head.distance(segment)<10:
                game_on=False
                score.game_over()
    
window.exitonclick()