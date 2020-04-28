"""
Class: ISTA 130
Section Leader: Pranav Talwar
These functions are for hw9
Date: 04/27/2020
Description: "fishcatch.txt" gives an explanation of the data in "fishcatch.dat". Read the explanation to understand what
 is in "fishcatch.dat". For this assignment we’ll only be interested in the name and weight of each fish in the ".dat"
file.
"""

def fish_dict_from_file(file):
    """
    Write a function called fish_dict_from_file that takes a single string parameter giving the name of a file to read.
    :param file: string
    :return: dictionary
    """
    fish_names = {
        '1': 'Bream',
        '2': 'Whitefish',
        '3': 'Roach',
        '4': '?',
        '5': 'Smelt',
        '6': 'Pike',
        '7': 'Perch',
    }

    read_file = open(file, 'r')
    fishes_map = {}

    for line in read_file.readlines():
        line_list = line.split(" ")
        filtered = list(filter(lambda x: x != "", line_list))
        the_name = fish_names[filtered[1]]
        if the_name not in fishes_map.keys():
            if filtered[2] != 'NA':
                fishes_map[the_name] = [float(filtered[2])]
        else:
            if filtered[2] != 'NA':
                fishes_map[the_name].append(float(filtered[2]))
    read_file.close()
    return fishes_map


def main():
    """
    prettify to print the fish table
    :return:
    """
    print("   # NAME          MEAN WT")
    fishes_map = fish_dict_from_file('fishcatch.dat')
    for key, value in sorted(fishes_map.items()):
        number_str = f"  {len(value)}".rjust(4)
        name_str = f" {key}".ljust(10)
        mean_str = f"{round(sum(value)/len(value), 1)}g".rjust(12)

        print(number_str+name_str+mean_str)


if __name__ == '__main__':
    main()
