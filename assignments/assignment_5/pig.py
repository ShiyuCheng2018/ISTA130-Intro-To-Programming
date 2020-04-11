'''
Name: Shiyu Cheng
Date: 04/03/2020
Class: ISTA 130
Section Leader: Pranav Talwar

Doc: For this program you will build a simple dice game called Pig. In this version of Pig, two players alternate turns.
Players each begin the game with a score of 0. During a turn a player will roll a six-sided die one or more times,
summing up the resulting rolls. At the end of the player’s turn the sum for that turn is added to the player’s total
 game score.

If at any time a player rolls a 1, the player’s turn immediately ends and he/she earns 0 points for that turn (i.e.
 nothing is added to the player’s total game score). This is called "pig". After every roll that isn't a 1, the player
  may choose to either end the turn, adding the sum from the current turn to his/her total game score, or roll again in
  an attempt to increase the sum.
'''
import random


def print_scores(name_1, score_1, name_2, score_2):
    '''
    print_scores that has four parameters – these hold, in this order, the name of the first player (a string), his/her
    score (an int), the second player's name (a string), and score (an int)
    :param name_1: string
    :param score_1: int
    :param name_2: string
    :param score_2: int
    :return:
    '''
    print(f"\n--- SCORES\t{name_1}: {score_1}\t{name_2}: {score_2} ---")

def check_for_winner(name, score):
    '''
    check_for_winner that has two parameters: a name (a string) and a score (an int):
    :param name: string
    :param score: int
    :return:
    '''
    if score >= 50:
        print(f"THE WINNER IS: {name}!!!!!")
        return True
    else:
        return False

def roll_again(name):
    '''
    roll_again that has a single string parameter to hold a player's name.
    :param name: string
    :return: boolean
    '''
    while True:
        wanna_roll_again = input(f"Roll again, {name}? (Y/N) ")
        if wanna_roll_again.upper() == "Y":
            return True
        elif wanna_roll_again.upper() == "N":
            return False
        else:
            print(f"I don't understand: \"{wanna_roll_again}\". Please enter either \"Y\" or \"N\".")

def play_turn(name):
    '''
    play_turn that has a single string parameter , which holds a player’s name
    :param name: string
    :return: boolean
    '''
    print(f"---------- {name}'s turn ----------")
    score = 0
    while True:
        roll = random.randint(1, 7)
        print(f"\t<<< {name} rolls a {roll} >>>")
        if roll == 1:
            print(f"\t!!! PIG! No points earned, sorry {name} !!!\n")
            score = 0
            input("(enter to continue)")
            return score
        elif roll > 1:
            score += roll
            print(f"\tPoints: {score}")
            if not roll_again(name):
                return score

def main():
    seed = input("Enter seed value: ")
    random.seed(seed)
    print()
    print()
    print("Pig Dice")
    player_1 = input("Enter name for player 1: ")
    player_2 = input("Enter name for player 2: ")
    print(f"\tHello {player_1} and {player_2}, welcome to Pig Dice!")
    score_1 = 0
    score_2 = 0

    while True:
        # print scores
        print_scores(player_1, score_1, player_2, score_2)
        # count score for player 1
        score_1 += play_turn(player_1)
        # if the score hits 50, then break
        if check_for_winner(player_1, score_1):
            break
        print_scores(player_1, score_1, player_2, score_2)
        # count score for player 2
        score_2 += play_turn(player_2)
        # if the score hits 50, then break
        if check_for_winner(player_2, score_2):
            break


main()



