import turtle
import math
'''
Author: Shiyu Cheng
Date: 1.30.2020
Class: ISTA 130
Section Leader: Pranav Talwar

Description:
User turtle.py to draw my name's initials "SYC"
'''

# put all of your import statements below this line and then delete this comment
import turtle
# put all of your function definitions below this line and then delete this comment

def draw_s(turtle):
    # S for "Shi"
    turtle.shape('turtle')
    turtle.pensize(10)
    turtle.setheading(90)
    turtle.penup()
    turtle.forward(120)
    turtle.setheading(180)
    turtle.pendown()
    turtle.forward(120)
    turtle.setheading(270)
    turtle.forward(120)
    turtle.setheading(0)
    turtle.forward(120)
    turtle.setheading(270)
    turtle.forward(120)
    turtle.setheading(180)
    turtle.forward(120)

def draw_y(turtle):
    # Y for "Yu"
    turtle.setheading(45)
    turtle.penup()
    turtle.forward(240*math.sqrt(2))
    turtle.pendown()
    turtle.setheading(300)
    turtle.forward(120)
    turtle.setheading(60)
    turtle.forward(120)
    turtle.backward(120)
    turtle.setheading(270)
    turtle.forward(140)

def draw_c(turtle):
    # C for "Cheng"
    turtle.setheading(45)
    turtle.penup()
    turtle.forward(240 * math.sqrt(2))
    turtle.setheading(180)
    turtle.pendown()
    turtle.forward(120)
    turtle.setheading(270)
    turtle.forward(240)
    turtle.setheading(0)
    turtle.forward(120)









#==========================================================
def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''
    # put main code here, make sure each line is indented one level, and delete this comment
    my_turtle = turtle.Turtle()
    my_turtle.shape('turtle')
    my_turtle.pensize(10)
    draw_s(my_turtle)
    draw_y(my_turtle)
    draw_c(my_turtle)
    turtle.getscreen().exitonclick()

if __name__ == '__main__':
    main()
