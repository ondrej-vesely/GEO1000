# GEO1000 - Assignment 2
# Authors: Ondrej Vesely, Giorgos Triantafyllou
# Studentnumbers: 5162130, 5381738


def wiggle(start, end, moves):
    length = abs(end - start)

    if length > moves:
        return 0
    if length == moves:
        return 1
    else:
        return 1 + ((moves-length)//2)*(length+1)


if __name__ == "__main__":
    print("running cab.py directly")
    print(wiggle(1, 4, 5))

