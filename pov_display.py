from turtle import *
import turtle
from pov_dissplay_algo import allCollisionPoints
from cart2pol import cart2pol

num_of_turtles = 30
led = []
position = []
#2d coordinates (radii,angle)
turn_on = allCollisionPoints((15,5),(-15,5),num_of_turtles)

#record all the positions of the led
positions = []
#all colors
colors = ['blue', 'green', 'black', 'red', 'yellow', 'cyan']

#intialising turtles
for i in range(num_of_turtles):
    led.append(turtle.Turtle())
#setting speed to fastest and bigger pensizes
for i in range(num_of_turtles):
    led[i].speed(0)
    led[i].pensize(5)

begin_fill()
turtle.colormode(255)

#leds to the down arm
for i in range(num_of_turtles):
    led[i].up()
    led[i].goto((i*10),0)
    led[i].left(90)


#move the leds in anti-clockwise
for angle in range(0,360,1):
    for i in range(num_of_turtles):
        #color only when needed
        position = i,angle
        if position in turn_on:
            led[i].down()
            led[i].pencolor(colors[3])
        else:
            led[i].up()
            led[i].pencolor(colors[2])
        #move the turtles in a circle with 1 degree at a time
        led[i].circle(i*10,1)

end_fill()

done()