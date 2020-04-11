'''
Author: Rich
Date: Eternity
Class: ISTA 130
Section Leader: I am maximum leader

Description:
Can you run this simple program?
'''

import turtle
def hmm(mighty_joe, size):

    mighty_joe.circle(size, 405)

    mighty_joe.lt(90)

    mighty_joe.fd(size * 2)

    mighty_joe.lt(90)

    mighty_joe.circle(size, 135)

def shaft(a_turtle, length):
    a_turtle.fd(length)
    
def arrowhead(trtl, side):
    trtl.rt(90)
    trtl.fd(side / 2)
    trtl.lt(120)
    trtl.fd(side)
    trtl.lt(120)
    trtl.fd(side)
    trtl.lt(120)
    trtl.fd(side / 2)
    trtl.lt(90)
    
def fletching(maximo, size):
    maximo.rt(120)
    maximo.fd(size / 3)
    maximo.rt(60)
    maximo.fd(size)
    maximo.rt(120)
    maximo.fd(size / 3)
    maximo.lt(60)
    maximo.fd(size / 3)
    maximo.rt(120)
    maximo.fd(size)
    maximo.rt(60)
    maximo.fd(size / 3)
    maximo.lt(60)

#==========================================================
def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''
    starlord = turtle.Turtle()
    starlord.speed(0)
    starlord.pencolor('magenta')
    starlord.pensize(10)
    turtle.bgcolor('darkblue')
   
    starlord.penup()
    starlord.goto(-100, 0)
    starlord.pendown()
    
    shaft(starlord, 200)
    
    arrowhead(starlord, 40)
    
    starlord.penup()
    starlord.goto(-100, 0)
    starlord.pendown()
    
    fletching(starlord, 60)

    size = 180

    starlord.penup()

    starlord.goto(size, 0)

    starlord.setheading(90)

    starlord.pendown()

    starlord.pensize(20)

    starlord.color('limegreen')

    hmm(starlord, size)
    
    
    turtle.getscreen().exitonclick()  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()
