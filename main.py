#!/usr/bin/env python3

import math

def start_up(file: str):
    with open(file, 'r') as f:
        contents = f.read()
        print(contents)

def input_prompt(measurement_type: str, side: str):
    return input(f"enter measurement for {measurement_type} {side} in inches:   ")

def construct_triangles(side_lengths: dict):
    triangle_A = [side_lengths["AC"], side_lengths["AB"], side_lengths["BC"]]
    triangle_D = [side_lengths["CD"], side_lengths["BD"], side_lengths["BC"]]
    triangle_B = [side_lengths["AB"], side_lengths["BD"], side_lengths["AD"]]
    triangle_C = [side_lengths["AC"], side_lengths["CD"], side_lengths["AD"]]
    return {"Triangle A": triangle_A, "Triangle B": triangle_B, "Triangle C": triangle_C, "Triangle D": triangle_D}


def calculate_angle(side_lengths: list):
    # Law of Cosines formula : cosA = (b^2 + c^2 - a^2)/2*b*c
    a = side_lengths[2]
    b = side_lengths[0]
    c = side_lengths[1]
    return math.degrees(math.acos(math.radians((b**2 + c**2 - a**2)/(2*b*c))))

def main():
    # Title Screen and diagram for visual aid
    start_up('title.txt')
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
        triangles[key] = calculate_angle(value)
        print(f"{key.replace('Triangle', 'Angle')}: {triangles[key]} degrees")


if __name__ == '__main__':
    main()
