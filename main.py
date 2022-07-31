#!/usr/bin/env python3

import math
import re
import sys
from fractions import Fraction
from functools import wraps


class WrongInputException(Exception):
    pass


def retry(error_message: str):
    def deco_retry(f):
        @wraps(f)
        def f_retry(*args, **kwargs):
            x = False
            while not x:
                try:
                    return f(*args, **kwargs)
                except WrongInputException:
                    print(error_message)
            return f(*args, **kwargs)
        return f_retry
    return deco_retry


def start_up(file: str):
    with open(f"{sys.path[0]}/{file}", 'r') as f:
        contents = f.read()
        print(contents)


def check_input(input_string: str):
    if re.search("^\d+\s\d{1,2}/\d{1,2}$", input_string):
        integer = re.search("^\d+\s", input_string).group().rstrip()
        fraction = Fraction(re.search("\s\d{1,2}\/\d{1,2}", input_string).group().lstrip())
        return int(integer) + fraction
    elif re.search("^\d+$", input_string):
        return int(re.search("^\d+$", input_string).group())
    else:
        raise WrongInputException


@retry(error_message='Input must be an integer or an integer/fraction')
def input_prompt(measurement_type: str, side: str):
    length = input(f"enter measurement for {measurement_type} {side} in inches:   ")
    return check_input(length)


def construct_triangles(side_lengths: dict):
    triangle_a = [side_lengths["AC"], side_lengths["AB"], side_lengths["BC"]]
    triangle_d = [side_lengths["CD"], side_lengths["BD"], side_lengths["BC"]]
    triangle_b = [side_lengths["AB"], side_lengths["BD"], side_lengths["AD"]]
    triangle_c = [side_lengths["AC"], side_lengths["CD"], side_lengths["AD"]]
    return {"Triangle A": triangle_a, "Triangle B": triangle_b, "Triangle C": triangle_c, "Triangle D": triangle_d}


def calculate_angle(side_lengths: list):
    # Law of Cosines formula : cosA = (a^2 - (b^2 + c^2))/ (-2*b*c)
    a = side_lengths[2]
    b = side_lengths[0]
    c = side_lengths[1]
    cos_a = (a**2 - (c**2 + b**2)) / (-2 * b * c)
    ans = math.acos(cos_a)
    return math.degrees(ans)


def start_routine():
    start_up('diagram.txt')
    # Instantiate dictionaries to store measurement values
    sides = {"AB": "", "CD": "", "AC": "", "BD": ""}
    diagonals = {"AD": "", "BC": ""}

    # Receive user input for measurements
    for s in sides:
        sides[s] = input_prompt(measurement_type="side", side=s)
    for d in diagonals:
        diagonals[d] = input_prompt(measurement_type="diagonal", side=d)

    # Merge dictionaries and divide the quadrilateral into triangles
    sides |= diagonals
    triangles = construct_triangles(sides)

    # Use Law of Cosines in the 4 triangles to solve for the corner angles in the quadrilateral
    for key, value in triangles.items():
        angle = calculate_angle(value)
        print(f"{key.replace('Triangle', 'Angle')}: {angle} degrees")


@retry(error_message='Input must be a Y or N')
def restart_program():
    ans = input("Would you like to start again? (Y/N):  ")
    if ans.capitalize() not in ["Y", "N"]:
        raise WrongInputException
    if ans.capitalize() == "Y":
        print("\033[H\033[J", end="")
        start_routine()
    else:
        sys.exit()


def main():
    # Title Screen and diagram for visual aid
    start_up('title.txt')
    input("Press enter to continue: ")
    start_routine()
    restart_program()


if __name__ == '__main__':
    main()
