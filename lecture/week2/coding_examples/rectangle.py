'''
Author: <your name>
Date: <the date>
Class: ISTA 130
Section Leader: <your section leader>

Description:
<summary of this program>
'''

# put all of your import statements below this line and then delete this comment
import turtle

def rectangle(turtle, width, height):
    turtle.setheading(0)
    turtle.forward(width)
    turtle.setheading(270)
    turtle.forward(height)
    turtle.setheading(180)
    turtle.forward(width)
    turtle.setheading(90)
    turtle.forward(height)


#==========================================================
def main():
    '''
    instance turtle module
    set shape and pen size
    call rectangle function
    '''
    m_turtle = turtle.Turtle()
    m_turtle.shape("turtle")
    m_turtle.pensize(10)
    rectangle(m_turtle, 100, 200)
    turtle.getscreen().exitonclick()  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()
