'''
Author: shiyu cheng
Date: 1.30.2020
Class: ISTA 130
Section Leader: Pranav Talwar

Description:
this is a program that draws yin and yang
'''

# put all of your import statements below this line and then delete this comment
import turtle
# put all of your function definitions below this line and then delete this comment

def draw(t,radius, color1, color2):
    '''
    this function is for draw a half of yin yang
    :param t: turtle
    :param radius: number
    :param color1: color string
    :param color2: color string
    :return:
    '''

    # half
    t.color("black")
    t.begin_fill()
    t.circle(radius/2, 180)
    t.circle(radius, 180)
    t.left(180)
    t.circle(-radius/2, 180)
    t.end_fill()

    # move to draw inside circle
    t.left(90)
    t.penup()
    t.forward(radius*0.35)
    t.right(90)
    t.pendown()

    # draw the inside circle
    t.color(color1, color2)
    t.begin_fill()
    t.circle(radius*0.15)
    t.end_fill()

    # reset the position
    t.left(90)
    t.penup()
    t.backward(radius*0.35)
    t.pendown()
    t.left(90)



#==========================================================
def main():
    '''
    draw yin yang
    '''
    t = turtle.Turtle()
    t.width(3)

    draw(t, 200, "black", "white")
    draw(t, 200, "white", "black")

    turtle.getscreen().exitonclick()  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()
