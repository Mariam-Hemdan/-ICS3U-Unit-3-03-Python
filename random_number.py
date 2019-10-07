#!/usr/bin/env python3

# Created by : Mariam Hemdan
# Created on : October 2019
# This module contains check the right random number


import random


def main():
    # This function check the right gusseing number

    # input
    random_number = random.randint(1, 9+1)  # a number between 1 and 10
    number_guessing_game = int(input("Enter a number from 0 to 9: "))
    print("")

    # process
    if number_guessing_game == random_number:
        # output
        print("you get it right")
    else:
        print("that is wrong ")


if __name__ == '__main__':
    main()
