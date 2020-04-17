'''
Class: ISTA 130
Section Leader: Pranav Talwar
These functions are for hw7
Date: 04/16/2020
'''


def print_report(file):
    '''
    this function is for printing the reports
    :param file: string
    :return: none
    '''

    # initial variables
    vowels_count = 0
    consonants_count = 0
    space_count = 0
    punctuation_count = 0

    # refactor variables
    vowels = 'aeiou'
    consonants = 'BCDFGHJKLMNPQRSTVXZWY'
    consonants += consonants.lower()
    vowels += vowels.upper()

    open_file = open(file, 'r')

    # loop through files and start to counting
    for line in open_file:
        for ch in line:
            if ch in vowels:
                vowels_count += 1
            elif ch in consonants:
                consonants_count += 1
            elif ch.isspace():
                space_count += 1
            else:
                punctuation_count += 1

    # calculations
    total = vowels_count + consonants_count + space_count + punctuation_count
    percent_vowels = round(vowels_count * 100 / total, 1)
    percent_consonants = round(consonants_count * 100 / total, 1)
    percent_space = round(space_count * 100 / total, 1)
    percent_punctuation = round(punctuation_count * 100/ total, 1)

    open_file.close()

    print()
    print(f'-------{file}------')
    print(f'Vowels:               {vowels_count}')
    print(f'Consonants:           {consonants_count}')
    print(f'Whitespace:           {space_count}')
    print(f'Punctuation:           {punctuation_count}')
    print(f'-------------------------')
    print(f'Total:                {total}\n')
    print(f'Percent vowels:      {percent_vowels}')
    print(f'Percent consonants:  {percent_consonants}')
    print(f'Percent spaces:      {percent_space}')
    print(f'Percent punctuation:  {percent_punctuation}')
    print(f'=========================')


def replace_parts_of_speech(line, replace):
    '''
    this function is for replace texts in a single line and return the new line
    :param line: string
    :param replace: string
    :return: string
    '''
    count = line.count(replace)
    for i in range(count):
        entry = input(f"Enter {replace.lower()}: ")  # ask user to input new words
        line = line.replace(replace, entry, 1)
    return line


def complete_mad_lib(file):
    '''
    This funtion is aiming for replace all actions in a complete story file!
    actions including ["PLURAL NOUN", "VERB PAST", "VERB", "NOUN", "ADJECTIVE"]
    :param file: string
    :return: none
    '''
    read_file = open(file, 'r')
    write_file = open(f"MAD_{file}", 'w')
    actions = ["PLURAL NOUN", "VERB PAST", "VERB", "NOUN", "ADJECTIVE"]  # actions array

    for line in read_file:
        for action in actions:
            line = replace_parts_of_speech(line, action)
        write_file.write(line)   # save new line
    read_file.close()
    write_file.close()


def main():
    '''
    call all functions !
    :return: none
    '''
    file = input("Enter file name: ")
    print_report(file)
    complete_mad_lib(file)

main()


