'''
Author: Sarah Stueve
Date: <the date>
Class: ISTA 130
Section Leader: I'm the (wo)man

Description:
The goal of this program is to write the word 'hello' using Turtle and by defining and calling functions.
'''

# put all of your import statements below this line and then delete this comment
import turtle
# put all of your function definitions below this line and then delete this comment
def draw_H(a_turtle):
    '''
    This function draws an H.
    Parameters:
        :a_turtle: turtle object
    Returns:
        None
    '''
    a_turtle.left(90)
    a_turtle.forward(100)
    a_turtle.backward(50)
    a_turtle.right(90)
    a_turtle.forward(50)
    a_turtle.left(90)
    a_turtle.forward(50)
    a_turtle.backward(100)

def draw_E(a_turtle):
    '''
    This function draws an E.
    Parameters:
        :a_turtle: turtle object
    Returns:
        None
    '''
    a_turtle.forward(50)
    a_turtle.backward(50)
    a_turtle.left(90)
    a_turtle.forward(100)
    a_turtle.right(90)
    a_turtle.forward(50)
    a_turtle.backward(50)
    a_turtle.right(90)
    a_turtle.forward(50)
    a_turtle.left(90)
    a_turtle.forward(50)

def draw_L(a_turtle):
    '''
    This function draws an L.
    Parameters:
        :a_turtle: turtle object
    Returns:
        None
    '''
    a_turtle.left(90)
    a_turtle.forward(100)
    a_turtle.backward(100)
    a_turtle.right(90)
    a_turtle.forward(50)

def draw_O(a_turtle):
    '''
    This function draws an O.
    Parameters:
        :a_turtle: turtle object
    Returns:
        None
    '''
    a_turtle.forward(50)
    a_turtle.left(90)
    a_turtle.forward(100)
    a_turtle.left(90)
    a_turtle.forward(50)
    a_turtle.left(90)
    a_turtle.forward(100)

def create_space(a_turtle):
    '''
    This function creates a space between two letters.
    Parameters:
        :a_turtle: turtle object
    Returns:
        None
    '''
    a_turtle.penup()
    a_turtle.forward(50)
    a_turtle.pendown()


#==========================================================
def main():
    '''
    Write the word "hello" using turtle.
    '''
    # put main code here, make sure each line is indented one level, and delete this comment

    # Configure turtle to your specifications (I chose to have my 'turtle' be in the shape of a turtle and increased pensize. You could also slow your turtle down to debug more easily.)
    tallulah = turtle.Turtle()
    tallulah.shape('turtle')
    tallulah.pensize(10)
    # tallulah.speed(1)

    # Draw H
    draw_H(tallulah)
    # Set turtle up to draw E
    tallulah.right(90)
    # Draw E
    create_space(tallulah)
    draw_E(tallulah)
    # Set turtle up to draw first L - we can't just create
    # space because of where we ended with the E. A better 
    # solution would be to draw the E a different way :-)
    tallulah.penup()
    tallulah.forward(50)
    tallulah.right(90)
    tallulah.forward(50)
    tallulah.left(90)
    tallulah.pendown()
    # Draw L
    draw_L(tallulah)
    # Draw L
    create_space(tallulah)
    draw_L(tallulah)
    # Draw O
    create_space(tallulah)
    draw_O(tallulah)
    

    turtle.getscreen().exitonclick()  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()