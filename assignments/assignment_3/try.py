'''
pseudocode:
1. define the function name and the argument: String
    1.1 assign an empty string to a variable name called result
    1.2 loop through the string that passed in as a local variable cha
        1.21 assign double times cha to the result
    1.3 print result to check if its expected
    1.4 return the result!
'''


def double_str(m_string):
    result = ''
    for cha in m_string:
        result += cha * 2
    print(result)
    return result

double_str('dog')
