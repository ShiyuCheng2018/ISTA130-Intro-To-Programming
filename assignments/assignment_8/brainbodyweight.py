"""
Class: ISTA 130
Section Leader: Pranav Talwar
These functions are for hw8
Date: 04/20/2020
"""


def find_insert_position(mammal, order_list):
    """
    Write a function called find_insert_position that takes two parameters. The first parameter is a string representing
    a terrestrial mammal’s name. The second parameter is a list of strings in alphabetical order.
    :param mammal: string
    :param order_list: list of strings
    :return: int
    """
    insert = 0
    if not order_list:  # mammal does not in the list
        return 0

    if mammal in order_list:  # if mammal already in the list
        return order_list.index(mammal)

    for name in range(0, len(order_list)):
        if order_list[name] < mammal:
            insert += 1
        else:  # found the insert index
            break

    return insert


def populate_lists(mammals, body_weights, brain_weights):
    """
    Write a function called populate_lists takes three parameters. The first parameter is a list to hold the mammal
     names. The second parameter is a list to hold the mammal body weights (these should be floats). The last list will
      hold the mammal brain weights (these should also be floats). This function must open the "BrainBodyWeightKilos.csv"
      file and then populate each list accordingly. The mammal names MUST be in title case.
    :param mammals: list of strings
    :param body_weights: list of strings
    :param brain_weights: list of strings
    :return: none
    """
    read_file = open("BrainBodyWeightKilos.csv", 'r')
    for line in read_file.readlines():
        line_list = line.split(",")  # get list
        mammals.append(line_list[0].title())
        body_weights.append(float(line_list[1]))
        brain_weights.append(float(line_list[2]))
    read_file.close()

def write_converted_csv(to_write, mammals, body_weights, brain_weights):
    """
    Write a function called write_converted_csv that takes four parameters. The first is the name of a file to write.
    The second is a list of strings (the names of mammals). The third is a list of floats (weights of mammals in
    kilograms). The fourth is a list of floats (brain weights of mammals in grams.)
    :param to_write: string
    :param mammals: list of strings
    :param body_weights: list of floats
    :param brain_weights: list of floats
    :return: none
    """
    write_file = open(to_write, 'w')

    for mammal in range(0, len(mammals)):
        # write a line is going to be inserted
        write_line = mammals[mammal].title()+","+str(round(body_weights[mammal] * 2.205, 2))+","+str(round(brain_weights[mammal] * 0.0022, 2))+'\n'
        write_file.write(write_line)


def main():
    """
        i.) Create three empty lists to hold mammal names, body weights, and brain weights.

        ii.) Populate the three empty lists you just created.

        iii.) Next you will repeatedly ask the user to (note that the prompt is preceded by a blank line): Enter animal
        name (or "q" to quit):

        Convert the user's response to title case. Depending on the user’s response:

        • If the name entered by the user is not in your list of names (case insensitive search):

        1.i. Print a message indicating the animal was not found.

        – For example, assuming the user entered "Bugbear" you would print:

        File does not contain "Bugbear".

        1.ii. Ask the user if he would like to add it. (You can assume the user will answer either ‘y’ or ‘n’.)

        – For example, assuming the user previously entered "Bugbear":

        Add "Bugbear" to file? (y|n)

        – If the user enters ‘n’, do nothing (i.e. you’ll go back to asking the user to enter an animal name)

        – If the user enters ‘y’, ask for the body weight and brain weight:

        - Continuing the previous example you would ask the user for each of the two following:

        Enter body weight for "Bugbear" in kilograms: Enter brain weight for "Bugbear" in grams:

        ∗ Add the new animal’s data to your three lists. Put the values in the appropriate positions in the lists so that
         the animals are still all alphabetized.

        • If the name entered by the user is already in your list of names: i. Print the animal’s data:

        – For example, assuming the user entered ‘Cat’

        Cat: body = 3.3, brain = 25.6

        ii. Ask the user if he would like to delete the animal. (You can assume the user will answer either ‘y’ or ‘n’.)

        – For example, assuming the user previously entered "Cat":

        Delete "Cat"? (y|n)

        – If the user enters ‘n’, do nothing (i.e. you’ll go back to asking the user to enter an animal name)

        – If the user enters ‘y’ delete the mammal’s data from your lists.

        • If the user entered 'q' you should:

        – use the function you wrote for part 2 above to write the data out to a new file called "BrainBodyWeightPounds.csv" and
        your program will end. If at any point you accidentally open this file with Excel, make sure you close it, because Excel
        will put a lock on it and you will not be able to write to it again until you close it.
    :return:
    """
    mammals = []
    body_weights = []
    brain_weights = []
    populate_lists(mammals, body_weights, brain_weights)

    while True:
        type_ = input('Enter animal name (or "q" to quit): ')
        type_name = type_.title()

        if type_name == "Q":
            write_converted_csv("BrainBodyWeightPounds.csv", mammals, body_weights, brain_weights)
            break

        elif type_name not in mammals:
            print(f'File does not contain "{type_name}".')
            user_answer = input(f'Add "{type_name}" to file? (y|n) ')
            if user_answer is "y":
                body_weight = input(f'Enter body weight for "{type_name}" in kilograms: ')
                brain_weight = input(f'Enter brain weight for "{type_name}" in grams: ')
                index = find_insert_position(type_name, mammals)
                mammals.insert(index, type_name)
                body_weights.insert(index, round(float(body_weight), 2))
                brain_weights.insert(index, round(float(brain_weight), 2))
                print()
            else:
                print()
        else:
            existed_index = mammals.index(type_name)
            print(f'{type_name}: body = {body_weights[existed_index]}, brain = {brain_weights[existed_index]}')
            if_delete = input(f'Delete "{type_name}"? (y|n) ')
            if if_delete is "y":
                mammals.remove(type_name)
                del body_weights[existed_index]
                del brain_weights[existed_index]
                print()
            else:
                print()

    write_converted_csv("BrainBodyPounds.csv", mammals, body_weights, brain_weights)


main()










