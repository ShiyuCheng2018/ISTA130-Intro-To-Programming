import turtle
import math
'''
Author: Shiyu Cheng
Date: 1.30.2020
Class: ISTA 130
Section Leader: Pranav Talwar

Description:
snake.py to draw a snake
'''

# put all of your import statements below this line and then delete this comment
import turtle
# put all of your function definitions below this line and then delete this comment

def draw_triangle(m_turtle, length):
    ''' this function is for drawing a triangle
    :param m_turtle: turtle
    :param length: number
    :return:
    '''
    m_turtle.color("green")
    m_turtle.setheading(210)
    m_turtle.forward(length)
    m_turtle.setheading(330)
    m_turtle.forward(length)
    m_turtle.setheading(90)
    m_turtle.forward(length)

def draw_square(m_turtle, length):
    '''
    this function is for drawing a square
    :param m_turtle: turtle
    :param length: number
    :return:
    '''

    m_turtle.color("black")

    for i in range(2):
        m_turtle.forward(length)
        m_turtle.right(90)
    m_turtle.forward(length)
    m_turtle.backward(length)

def hexagon(m_turtle, length):
    '''
    this function is for drawing a hexagon
    :param m_turtle: turtle
    :param length: number
    :return:
    '''
    m_turtle.setheading(90)
    m_turtle.forward(length)
    m_turtle.setheading(330)
    m_turtle.color("red")
    m_turtle.forward(length*2)
    m_turtle.setheading(90)
    m_turtle.forward(length)
    m_turtle.setheading(210)
    m_turtle.forward(length*2)
    m_turtle.setheading(90)
    m_turtle.color("black")
    m_turtle.forward(length)
    m_turtle.setheading(30)
    m_turtle.color("goldenrod")
    m_turtle.forward(length)
    m_turtle.setheading(330)
    m_turtle.forward(length)

    m_turtle.penup()
    m_turtle.setheading(270)
    m_turtle.forward(length)
    m_turtle.pendown()

    m_turtle.color("goldenrod")
    m_turtle.setheading(210)
    m_turtle.forward(length)
    m_turtle.setheading(150)
    m_turtle.forward(length)

    #back to angle
    m_turtle.backward(length)
    m_turtle.setheading(30)
    m_turtle.forward(length)
    m_turtle.setheading(0)

def pentagon(m_turtle, length):
    '''
    this function is for drawing pentagon
    :param m_turtle:
    :param length:
    :return:
    '''
    m_turtle.left(90)
    m_turtle.color("black")
    for i in range(5):
        m_turtle.forward(length)
        m_turtle.right(72)

#==========================================================
def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''
    # put main code here, make sure each line is indented one level, and delete this comment
    leonardo = turtle.Turtle()
    leonardo.shape('turtle')
    leonardo.pensize(5)
    leonardo.speed(10)

    draw_triangle(leonardo, 50)

    leonardo.setheading(0)
    draw_square(leonardo, 50)

    hexagon(leonardo, 50)
    hexagon(leonardo, 50)

    pentagon(leonardo, 50)

    # keep open the drawing window
    turtle.getscreen().exitonclick()

if __name__ == '__main__':
    main()
