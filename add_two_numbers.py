#!/usr/bin/env python3

# Created by: Venika Sem
# Created on: oct 2022
# This program add two numbers inputted from the user

import math


def main():
    # this function adds two numbers

    # input
    first_integer = int(input("Enter first integer: "))
    second_integer = int(input("Enter second integer: "))

    # process
    sum_of_integers = first_integer + second_integer

    # output
    print("")
    print("{0} + {1} = {2}.".format(first_integer, second_integer, sum_of_integers))

    print("\nDone.")


if __name__ == "__main__":
    main()
