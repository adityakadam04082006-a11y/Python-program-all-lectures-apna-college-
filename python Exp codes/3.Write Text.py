
    
from turtle import*
import colorsys

bgcolor("black")
speed(0)
penup()
goto(-250,0)

text = "Aditya"
h = 0.0

for ch in text:
    color(colorsys.hsv_to_rgb(h,1,1))
    write(ch ,font=("Arial",48,"bold"))
    forward(40)
    h += 0.15

done()    

