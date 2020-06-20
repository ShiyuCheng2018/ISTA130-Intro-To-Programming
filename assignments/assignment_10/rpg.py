"""
Class: ISTA 130
Section Leader: Pranav Talwar
These functions are for hw10
Date: 05/06/2020
Description: In this assignment you will write a program to simulate combat for a simple Role Playing Game (RPG). The
game will have a single type of character, the Fighter. Each individual Fighter will have an integer value called “hit
points” that represents his/her current health (the amount of damage he/she can sustain before death).
"""

import random


class Fighter:

    def __init__(self, name):
        """
        Write an initializer method called __init__ that takes 2 parameters: self (all of your methods will have this
        as the first parameter), and name (a string, the name of a fighter). The initializer method will:
        :param name: string
        """
        self.name = name
        self.hit_points = 10

    def __repr__(self):
        """
        Write a method called __repr__ that takes one parameter: self. The method returns a string showing the name and
        hit points of the instance in the following format:
        :return:
        """
        return f'{self.name} (HP: {self.hit_points})'

    def take_damage(self, damage_amount):
        """
        Write a method called take_damage that takes two parameters: self (the Fighter instance that calls the method),
         and damage_amount (an integer representing the number of hit points of damage that have just been inflicted on
          this Fighter):
        :param damage_amount: int
        :return:
        """
        self.hit_points -= damage_amount

        if self.hit_points > 0:
            print(f'\t{self.name} has {self.hit_points} hit points remaining.')
        else:
            print(f'\tAlas, {self.name} has fallen!')

    def attack(self, other):
        """
        Write a method called attack that takes two parameters: self (the Fighter instance that calls the method), and
         other (another Fighter instance being attacked by self)
        :param other: Fighter
        :return:
        """
        print(f'{self.name} attacks {other.name}!')
        attack = random.randrange(1, 21)

        if attack >= 12:
            attack = random.randrange(1, 7)
            print(f'\tHits for {attack} hit points!')
            other.take_damage(attack)
        else:
            print('\tMisses!')

    def is_alive(self):
        """
        Write a method called is_alive that takes one parameter: self (the Fighter instance that calls the method).
        :return: Boolean
        """
        return True if self.hit_points > 0 else False


def combat_round(fighter_1, fighter_2):
    """
    Outside of the class write a function called combat_round that takes two parameters. The first is an instance of
    Fighter. The second is another instance of Fighter.
    :param fighter_1:
    :param fighter_2:
    :return:
    """
    num_1 = random.randrange(1, 7)
    num_2 = random.randrange(1, 7)
    if num_1 == num_2:
        print('Simultaneous!')
        fighter_1.attack(fighter_2)
        fighter_2.attack(fighter_1)

    elif num_1 > num_2:
        fighter_1.attack(fighter_2)
        if fighter_2.is_alive():
            fighter_2.attack(fighter_1)
    else:
        fighter_2.attack(fighter_1)
        if fighter_1.is_alive():
            fighter_1.attack(fighter_2)


def main():
    """
    a.) Create two instances of the Fighter class. The name of the first fighter must be Death_Mongrel; the second must
     be Hurt_then_Pain.

    ii.) Next repeat the following process until one (or both) fighters have been slain (remember, a Fighter is dead when
     it has less than 1 hit point):

    a.) Print the combat round number (start with 1) as shown in the following example:

    ====================== ROUND 1 ======================

    NOTE: There are 19 equal signs on each side

    b.) Print each Fighter’s information (remember how the __ repr__ method works). E.g.:

    Bonzo (HP: 4) Chubs (HP: 7)

    c.) Use the input function to pause the program (like we did in our turtle graphics programs) until the user presses
     enter. Prompt the user with the following message:

    Enter to Fight!

    d.) Use your combat_round function to simulate a single round of combat.
    :return:
    """
    fighter_1 = Fighter("Death_Mongrel")
    fighter_2 = Fighter("Hurt_then_Pain")

    game_round = 0

    while fighter_1.hit_points >= 1 and fighter_2.hit_points >= 1:
        game_round += 1
        print(f"\n=================== ROUND {game_round} ===================")

        # a
        print(fighter_1)
        print(fighter_2)

        # b
        input("Enter to Fight!")

        # c
        combat_round(fighter_1, fighter_2)

    print()
    print("The battle is over!")
    print(fighter_1)
    print(fighter_2)


if __name__ == '__main__':
    main()
