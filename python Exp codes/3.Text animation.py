from turtle import *
import colorsys
import math

screen = Screen()
screen.bgcolor("black")
screen.tracer(0)

hideturtle()
penup()

text = "Aditya"
font_size = 88
goto(0, 0)

h = 0.6
t = 0

while True:
    clear()

    # shadow
    goto(3, -3)
    color("black")
    write(text, align="center",
          font=("Arial", font_size, "bold"))

    # glow
    for i in range(6, 0, -1):
        goto(0, -i)
        color(colorsys.hsv_to_rgb(h, 0.6, 0.3))
        write(text, align="center",
              font=("Arial", font_size, "bold"))

    # main shine
    brightness = 0.7 + 0.3 * math.sin(t)    #this math.sin(t) used for smooth wave so
    goto(0, 0)                              #brightness changes 
    color(colorsys.hsv_to_rgb(h, 1, brightness))
    write(text, align="center",
          font=("Arial", font_size, "bold"))

    h += 0.001
    if h > 0.75:
        h = 0.6

    t += 0.05
    screen.update()
