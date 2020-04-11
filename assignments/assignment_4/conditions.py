'''
Name: Shiyu Cheng
Date: 02/27/2020
Class: ISTA 130
Section Leader: Pranav Talwar
These functions are for hw4
'''

def word_length(words, num):
    '''
    Using what you just learned about the len function, write a function called word_length that has two parameters.
     The first will be a string and the second will be an integer. The function first prints a message about the
     relationship between the length of the word and the integer, as shown in the following examples.
    :param words: string
    :param num: int
    :return: none
    '''
    if len(words) > num:
        result = "Longer than"
    elif len(words) < num:
        result = "Shorter than"
    else:
        result = "Exactly"
    print(f"{result} {num} characters: {words}")


def stop_light(light, num):
    '''
    Write a function called stop_light that determines whether a stop light should change color, and, if so, what color
    it should change to. It takes two arguments. The value of the first will be either "green", "yellow", or "red". This
    represents the stop light's current color. The second parameter tells the function how long this color has been
     showing. If green has been showing longer than 60 seconds, return "yellow". If yellow has been showing longer than
     5 seconds, return “red”. If red has been showing longer than 55 seconds, return “green”. If the color hasn’t been
     showing long enough (e.g. green has been showing for 17 seconds), return the current color.
    :param light: string
    :param num: int
    :return: string
    '''
    if light == "yellow" and num > 5 or light == "red" and num < 55:
        return "red"
    elif light == "yellow" and num <= 5 or light == "green" and num > 60:
        return "yellow"
    else:
        return "green"


def is_normal_blood_pressure(systolic, diastolic):
    '''
    Write a function called is_normal_blood_pressure that has two integer parameters.The first represents systolic blood
    pressure (the top number in a blood pressure reading). The second represents diastolic blood pressure (the bottom
    number in a blood pressure reading). The function should return True if systolic is less than 120 and diastolic is
    less than 80 (i.e. blood pressure is normal). Otherwise it returns False.
    :param systolic: int
    :param diastolic: nit
    :return: boolean
    '''
    if systolic < 120 and diastolic < 80:
        return True
    else:
        return False


def doctor():
    '''
    Write a function called doctor that has no parameters. The function will ask the user to enter his/her systolic
    blood pressure reading. It will then ask for the diastolic reading. The function then prints either “Your blood
    pressure is normal.” or “Your blood pressure is high.” depending on the values entered. This function should use
     the function you wrote in the previous question.
    :return: none
    '''
    systolic = input("Enter your systolic reading: ")
    diastolic = input("Enter your diastolic reading: ")
    result = is_normal_blood_pressure(systolic, diastolic)
    if result:
        print(f"Your blood pressure is normal.")
    else:
        print(f"Your blood pressure is high.")


def pants_size(size):
    '''
    Write a function called pants_size that has a single parameter (the value will be an integer) representing a
    person’s waist size in inches. The function returns a string. The string returned will be either "small", "medium",
    or "large" depending on the parameter value. Waist measurements that are 34 inches or larger should return large.
    Measurements that are 30 inches or larger, but not large enough to be in the large category, should return medium.
     Anything smaller should return small.
    :param size: inr
    :return: string
    '''
    if size >= 34:
        return "large"
    elif size >= 30:
        return "medium"
    else:
        return "small"


def pants_fitter():
    '''
    Write a function called pants_fitter that takes no arguments. The function should first ask the user for his/her
    name. It then greets the user by name. Next it asks the user for his/her waist size in inches (a positive integer).
     It then asks the user how many pairs of pants he/she would like to buy (a positive integer). Next it asks what type
     of pants the user wants to buy (either “regular” or “fancy”). Next it calculates the cost of the pants (integer).
      Regular pants cost $40 per pair. Fancy pants cost $100 per pair. Finally it prints out the number of pairs,
      the size, the type, and the total cost. The following examples show the format that your prompts and output should be in. This function should use the function you wrote in the previous question.
    :return: none
    '''
    name = input("Enter your name: ")
    print(f"Greetings {name} welcome to Pants-R-Us")
    size = input("Enter your size: ")
    amount = input("How many pairs of pants would you like: ")
    pants_type = input("Would you like regular or fancy pants? ")

    print(f"{amount} pairs of {pants_size(size)} {pants_type} pants: $ {100 * amount}")\
        if pants_type == "fancy" else print(f"{amount} pairs of {pants_size(size)} {pants_type} pants: $ {40 * amount}")


def digdug(num):
    '''
    Write a function called beef_type that takes a single parameter, percent_lean. If the value of percent_lean is less
     than 78%, return "Hamburger". If it is at least 78% and less than 85%, then return "Chuck". At least 85% but less
     than 90% return "Round". 90-95% inclusive return "Sirloin". If percent_lean doesn’t fall within one of these
     ranges, return "Unknown".
    :param num: int
    :return: none
    '''
    for i in range(1, num+1):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{i} : digdug")
        elif i % 3 == 0:
            print(f"{i} : dig")
        elif i % 5 == 0:
            print(f"{i} : dug")


def beef_type(num):
    '''
    Write a function called beef_type that takes a single parameter, percent_lean. If the value of percent_lean is less
    than 78%, return "Hamburger". If it is at least 78% and less than 85%, then return "Chuck". At least 85% but less
     than 90% return "Round". 90-95% inclusive return "Sirloin". If percent_lean doesn’t fall within one of these ranges,
      return "Unknown".
    :param num: float
    :return: string
    '''
    if num < 78:
        return "Hamburger"
    elif 78 <= num < 85:
        return "Chuck"
    elif 85 <= num < 90:
        return "Round"
    elif 90 <= num <= 95:
        return "Sirloin"
    else:
        return "Unknown"


def species_height(race, height):
    '''
    Write a function called species_height that takes 2 arguments. The first is either "Human" or "Klingon". The second
    is a positive float representing the height (in inches) of this human or Klingon. In this homework assignment, the
    average human height is 67 inches. The average Klingon height is 71 inches. For the parameters given, print out if
    it is above, below or at the average height for its species.
    :param race: string
    :param height: string
    :return: none
    '''
    if race == "Human":
        if height == 67:
            print("Average")
            return
        print("Below Average") if height < 67 else print("Above Average")
    else:
        if height == 71:
            print("Average")
            return
        print("Below Average") if height < 71 else print("Above Average")


def sooner_date(month_1, day_1, month_2, day_2):
    '''
    Write a function called sooner_date that has 4 integer parameters. The first is a number between 1 and 12
    (inclusive) that represents a month. 1 is January, 2 is February, etc. The second is a number between 1 and 31
    (inclusive) that represents a day. The third parameter is another integer representing a month and the fourth is
     another integer parameter representing a day. So essentially you have 2 dates (the first 2 parameters and the
     second 2 parameters). Figure out which date would come sooner, then print out that date in the format month / day.
    :param month_1: int
    :param day_1: int
    :param month_2: int
    :param day_2: int
    :return: none
    '''
    if month_1 == month_2:
        print(f"{month_1} / {day_1}") if day_2 > day_1 else print(f"{month_2} / {day_2}")
    else:
        print(f"{month_1} / {day_1}") if month_2 > month_1 else print(f"{month_2} / {day_2}")


