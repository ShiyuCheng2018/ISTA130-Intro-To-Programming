'''
Name: Shiyu Cheng
Date: 02/13/2020
Class: ISTA 130
Section Leader: Pranav Talwar

This is functions frm hw3
'''
import math

def print_word(num, m_string):
    '''
    The first is an integer (assume it will always be non-negative). The second is a string. Print the string on the
     given number of lines, each time preceded by a line number and an arrow.
    :param num: int
    :param m_string: string
    :return:none
    '''
    for i in range(1,num+1):
        print(f'{i} --> {m_string}')

def bacteria(time, num):
    '''
    The function has two parameters. The first is an integer giving the number of minutes it takes for a bacterium to
    split into two new bacteria. The second is an integer giving the number of bacterial generations to include in
     the output.
    :param time:int
    :param num:int
    :return:none
    '''
    m_sum = 2

    for i in range(1,num+1):
        print(f'after {time*i} minutes:  {m_sum} bacteria')
        m_sum += m_sum

def convert_to_copper(num1, num2, num3):
    '''
    The second represents a number of silver coins. The third represents a number of copper coins. The function will
    print the numbers of each type of coin followed by the total value of all of the coins when converted to copper.
    :param num1:int
    :param num2:int
    :param num3:int
    :return:none
    '''
    print(f'{num1} gp, {num2} sp, {num3} cp converted to copper is: {num1*10*5+num2*5+num3} cp')

def convert_from_copper(num):
    '''
    The function prints out the number of gold pieces (gp), silver pieces (sp), and copper pieces (cp) you would end up
     with if you first converted as many of the initial copper pieces to gold as possible and then converted as many of
      the remaining copper pieces as possible to silver pieces.
    :param num:int
    :return:none
    '''
    gp = num // 50
    sp = (num - gp*50) // 5
    cp = num - gp*50 - sp*5
    print(f'{num} copper pieces is: {gp} gp, {sp} sp, {cp} cp')

def repeat_word(m_string, row, col):
    '''
    The second is for an integer representing a number of rows. The third is for an integer representing a number of
     columns. The function prints the word in a number of rows equal to the value of the rows parameter and each row
     contains the word repeated a number of times equal to the columns parameter.
    :param m_string:string
    :param row:int
    :param col:int
    :return:none
    '''
    for i in range(row):
        for j in range(col):
            print(m_string, end='')
        print()

def text_triangle(num):
    '''
    Using what you learned in the previous question, write a function called text_triangle that takes an integer
     parameter and prints X’s in a triangle shape.
    :param num:int
    :return:none
    '''
    j = 1
    if num > 0:
        for i in range(1, num+1):
            print('X'*j)
            j += 1
    else:
        print()

def surface_area_of_cylinder(num1, num2):
    '''
    The first is a float representing the radius of a cylinder. The second is a float representing the height of a
    cylinder. The function calculates and prints the surface area of a cylinder with the given radius and height.
    :param num1:int
    :param num2:int
    :return:none
    '''
    print(f'The surface area of a cylinder with radius {num1} and height {num2} is '
          f'{2*math.pi*num1*num1+2*math.pi*num1*num2}')

def tree_height(distance, k_string):
    '''
    The first is a float representing the distance from you to the base of the tree. The second is a float representing
     the length of the kite string. The function will calculate and print the height of the tree as shown in the examples
      below. The function will calculate and print the height of the tree.
    :param distance:int
    :param k_string:int
    :return:none
    '''
    print(f'Kite string: {k_string}\n'
          f'Distance: {distance}\n'
          f'Height: {math.sqrt(k_string*k_string - distance*distance)}')
