'''
Class: ISTA 130
Section Leader: Pranav Talwar
These functions are for hw6
Date: 04/09/2020
'''

def US_to_EU(date):
    '''
    This function takes a string representing a US style date and returns a European style date string (if it takes an
    argument, it must have a corresponding parameter).
    :param date: string
    :return: string
    '''
    date_list = date.split("/")
    return f"{date_list[1]}.{date_list[0]}.{date_list[2]}"

def is_phone_num(num_string):
    '''
    This Boolean function takes a string and returns True if it is in the format dddddd-dddd, where d is a digit,
    False otherwise.
    :param num_string:string
    :return:boolean
    '''
    num_list = num_string.split('-')
    if len(num_list) != 3:
        return False
    elif len(num_list[0]) != 3 or len(num_list[1]) != 3:
        return False
    elif len(num_list[2]) != 4:
        return False

    for num in num_list:
        for each in num:
            if each not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                return False
    return True


def redact_line(line):
    '''
    This function takes a string and returns a new string that has all of the phone numbers (as defined in the previous
     function description) in the original string replaced by 'XXX-XXX-XXXX'. Assume that the argument ends in a newline.
    :param line: string
    :return: string
    '''
    for i in range(len(line) - 12):
        if (i == 0 or line[i - 1] == ' ') and line[i + 12] in ' \n' and\
                is_phone_num(line[i:i + 12]): line = line[:i] + line[i:].replace(line[i:i + 12], "XXX-XXX-XXXX", 1)
    return line


def redact_file(filename):
    '''
    This function takes a string filename. It writes a new file that has the same contents as the argument, except that
    all of the phone numbers are redacted.
    :param filename:string
    :return: out put a file
    '''
    read_file = open(filename, 'r')
    name = filename[:-4]+"_redacted.txt"
    write_file = open(name,'w')
    for line in read_file:
        write_file.write(redact_line(line))
    read_file.close()
    write_file.close()

def plagiarism(file_1, file_2):
    '''
    This Boolean function takes two filenames. If any line occurs in both files, return True. If not, return False.
    :param file_1:string
    :param file_2:string
    :return:boolean
    '''
    read_file_1 = open(file_1, 'r')
    for line1 in read_file_1:
        read_file_2 = open(file_2, 'r')
        for line2 in read_file_2:
            if line1 == line2:
                return True
        read_file_2.close()

    read_file_1.close()
    return False



def count_word(filename, keyword):
    '''
    This function takes a filename and a keyword. Return the number of times the keyword occurs in the file. Initialize
    a variable to keep track of the number of times the keyword appears. Traverse the file by line. Use the count method
    on each line to find the number of times the keyword appears in it and add that amount to the variable.
    :param filename: string
    :param keyword: string
    :return: int
    '''
    read_file = open(filename, 'r')
    sum = 0
    for line in read_file:
        sum += line.count(keyword)

    return sum



