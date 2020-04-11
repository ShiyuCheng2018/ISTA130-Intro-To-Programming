'''
Author: Rich
Date: Eternity
Class: ISTA 130
Section Leader: I am maximum leader

Description:
Can you run this simple program?
'''

import math

#==========================================================
def main():
    '''
    Call erfc.
    '''
    x = float(input('Enter x: '))
    precision = int(input('Enter precision: '))
    print(round(math.erfc(x), precision))
    
if __name__ == '__main__':
    main()
