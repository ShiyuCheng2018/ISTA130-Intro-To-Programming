'''
Author: Sarah Stueve
Date: <the date>
Class: ISTA 130
Section Leader: I'm the (wo)man

Description:
The goal of this program is to write the word 'hello' using Turtle.
'''

# put all of your import statements below this line and then delete this comment
import turtle
# put all of your function definitions below this line and then delete this comment


#==========================================================
def main():
    '''
    Write the word "hello" using turtle.
    '''
    # put main code here, make sure each line is indented one level, and delete this comment
    # configure turtle to your specifications (I chose to have my 'turtle' be in the shape of a turtle and increase pensize)
    tallulah = turtle.Turtle()
    tallulah.shape('turtle')
    tallulah.pensize(10)

    # Draw H
    tallulah.left(90)
    tallulah.forward(100)
    tallulah.backward(50)
    tallulah.right(90)
    tallulah.forward(50)
    tallulah.left(90)
    tallulah.forward(50)
    tallulah.backward(100)

    # Draw E
    tallulah.right(90)
    tallulah.penup()
    tallulah.forward(50)
    tallulah.pendown()
    tallulah.forward(50)
    tallulah.backward(50)
    tallulah.left(90)
    tallulah.forward(100)
    tallulah.right(90)
    tallulah.forward(50)
    tallulah.backward(50)
    tallulah.right(90)
    tallulah.forward(50)
    tallulah.left(90)
    tallulah.forward(50)

    # Draw L
    tallulah.penup()
    tallulah.forward(50)
    tallulah.left(90)
    tallulah.forward(50)
    tallulah.pendown()
    tallulah.backward(100)
    tallulah.right(90)
    tallulah.forward(50)

    # Draw L
    tallulah.penup()
    tallulah.forward(50) # oops! I made a mistake. The pen was still up when I started to draw! call pendown()
    tallulah.pendown()
    tallulah.left(90)
    tallulah.forward(100)
    tallulah.backward(100)
    tallulah.right(90)
    tallulah.forward(50)

    # Draw O
    tallulah.penup()
    tallulah.forward(50)
    tallulah.pendown()
    tallulah.forward(50)
    tallulah.left(90)
    tallulah.forward(100)
    tallulah.left(90)
    tallulah.forward(50)
    tallulah.left(90)
    tallulah.forward(100)

    turtle.getscreen().exitonclick()  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()