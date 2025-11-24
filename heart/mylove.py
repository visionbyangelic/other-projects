import math
from turtle import * # import everything from turtle module

def love1(k): # define love1 function
    return 15 * math.sin(k) ** 3 

def love2(k):
    return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k) 

speed(0) # set turtle speed to 0
bgcolor("black") # set background color to black

penup()

setheading(0) # set turtle direction to right
goto(0, 0)
pendown()


for i in range(100000):
    x = love1(i) * 20
    y = love2(i) * 20
    goto(x, y)
    for j in range(2):
        color("pink")
        goto(x, 0)
        
done()
