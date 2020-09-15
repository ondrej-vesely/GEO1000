from cab import wiggle

# This file can be used to test the wiggle function
# It's *not* to be handed in
#
# It also acts as a demo of the if statement using the
# special __name__ variable inside cab.py
#
# if __name__ == "__main__":
#     pass
#
# More info about this: https://youtu.be/sugvnHA7ElY
# (note, that video is using Python2 syntax, 
# so missing parenthesis to print() statements)


def test_wiggle():
    assert wiggle(1, 4, 5) == 5


print("running wiggle function in cab.py via import")
test_wiggle()
