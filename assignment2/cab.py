# GEO1000 - Assignment 2
# Authors: Ondrej Vesely, Giorgos Triantafyllou
# Studentnumbers: 5162130, 5381738


def wiggle(start, end, moves):
    length = abs(end - start)

    if length > moves:
        # too short
        return 0
    elif length == moves:
        # straight path
        return 1    
    elif (length - moves)%2 == 1:
        # one move too many
        return 0
    else:
        # count number of reverse steps and their permutations
        product = 1
        for n in range(moves, moves - (length-moves)//2):
            product = product * n
        return product


if __name__ == "__main__":
    print("running cab.py directly")
    print(wiggle(1, 4, 5))

