import random
from turtle import Turtle, Screen
tim = Turtle()
colours = ["red", "green", "blue", "grey", "yellow", "orange", "pink", "magenta", "brown"]
tim.speed("fastest")
for _ in range(3, 11):
    k = random.choice(colours)
    tim.color(k)
    for i in range(_):
        tim.forward(100)
        tim.right(360/_)








screen = Screen()
Screen().exitonclick()