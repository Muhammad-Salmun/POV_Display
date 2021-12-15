from turtle import *
import turtle
from pov_dissplay_algo import allCollisionPointsInCart

num_of_turtles = 30
ledOnPoints = []

turn_on = allCollisionPointsInCart((-15,15),(15,-15),num_of_turtles)

turtle.speed(0)
turtle.pensize(2)
turtle.up()

for i in turn_on:
        for elements in i:
                ledOnPoints.append(elements*15)
        turtle.goto(ledOnPoints)
        ledOnPoints.clear()
        turtle.dot()
        turtle.up()

turtle.goto(0,0)

done()

