'''
Name: Shiyu Cheng
Date: 02/06/2020
Class: ISTA 130
Section Leader: Pranav Talwar

Put your header comments here.
'''

""" 
    *********************************
    Answers to questions:
    1) The sum of the arguments is: 11112142
    2) Chance of rain today: 81 %
    3) Chance of rain today: 14 %
    4) The angle in radians is: 1.571
    5) The angle in radians is: 3.142
    6) Result: 2.293
    7) Result: 3.902
    8) Result: 9.626
    ********************************* 
"""

import math, random

# Put your function definitions below this line:


def chases(string_1, string_2):
    print(f"The {string_1} chases the {string_2}")


def sum3(num1, num2, num3):
    print(f"The sum of the arguments is: "+str(num1+num2+num3))


def forecast():
    print(f"Chance of rain today: {random.randrange(101)} %")


def radians(degrees):
    print(f"The angle in radians is: {round(degrees * math.pi / 180, 3)}")


def decimal(num):
    print(f"Decimal part: {round(num - math.floor(num), 3)}")


def erf_plus_gamma(num):
    print(f"Result: {round(math.erf(num)+math.gamma(num), 3)}")

