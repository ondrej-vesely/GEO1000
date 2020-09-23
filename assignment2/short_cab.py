# GEO1000 - Assignment 2
# Authors: Ondrej Vesely, Giorgos Triantafyllou
# Studentnumbers: 5162130, 5381738


def wiggle(start, end, moves):
    length = abs(end - start)
    if length > moves or (length - moves)%2:
        return 0
    else:
        product = 1
        for n in range(moves, moves - (length-moves)/2):
            product = product * n
        return product


if __name__ == "__main__":
    print("running cab.py directly")
    print(wiggle(1, 4, 5))

