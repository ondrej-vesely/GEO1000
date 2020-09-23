# GEO1000 - Assignment 2
# Authors: Ondrej Vesely, Giorgos Triantafyllou
# Studentnumbers: 5162130, 5381738

import string


def sentence_value(sentence):
    sum = 0
    for char in sentence.lower():
        if char.isalpha():
            sum += 1 + string.ascii_lowercase.index(char)
    return sum


def rds(value):
    sum = 0
    for char in str(value):
        if char.isdigit():
            sum += int(char)
    if sum >= 10:
        return rds(sum)
    else:
        return sum


if __name__ == "__main__":
    initial_integer = sentence_value("Geomatics is fun!")
    result = rds(initial_integer)
    print(result)
