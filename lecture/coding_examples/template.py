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
# put all of your function definitions below this line and then delete this comment

def draw(t, color_1, color_2, color_3,color_4):



    t.pencolor(color_1)
    t.pensize(10)
    t.right(45)
    t.forward(120)
    t.right(90)
    t.pencolor(color_2)
    t.forward(120)
    t.right(90)
    t.pencolor(color_3)
    t.forward(120)
    t.right(90)
    t.pencolor(color_4)
    t.forward(120)
#==========================================================
def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''
    # put main code here, make sure each line is indented one level, and delete this comment
    t = turtle.Turtle()
    t.reset()
    draw(t,'green', 'purple', 'red', 'yellow')

    # draw_yinyang(t=turtle.Turtle())

    turtle.getscreen().exitonclick()  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()
