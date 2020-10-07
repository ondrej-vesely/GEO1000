# GEO1000 - Assignment 3
# Authors: Ondrej Vesely, Giorgos Triantafyllou
# Studentnumbers: 5162130, 5381738

def reverse_part(part):
    """Take as input a list
    Returns a new list with elements in input reversed
    Note: Pure function, so should not modify input!
    
    Example:
    
        >>> reverse_part(['t', 'h', 'i', 's'])
        ['s', 'i', 'h', 't']
    """
    return reversed(part)


def part_to_str(part):
    """Take as input a list with letters.
    Returns a new string with letters in the input list

    Example:

        >>> part_to_str(['a', 'b', 'c'])
        "abc"

    """
    return ''.join(part)


def split_in_parts(sentence):
    """Split the string into a list of lists (either containing letters, or just
    one character not part of the alphabet).

    Example:

        >>> split_in_parts("this  is.")
        [['t', 'h', 'i', 's'], [' '], ['i', 's'], ['.']]
    """
    total_list = []
    sub_list=[]

    for char in sentence:
        if char.isalpha():
            sub_list.append(char)
        else:
            if sub_list:
                total_list.append(sub_list)
                sub_list = []
            total_list.append([char])
    
    return total_list

        
def reverse_relevant_parts(parts):
    """Reverse only those sublists consisting of letters
    
    Input: list of lists, e.g. [['t', 'h', 'i', 's'], [' '], ['i', 's'], ['.']]
    Returns: list with sublists reversed that consist of letters only.
    """
    return [reverse_part(part) if part_to_str(part).isalpha()
            else part for part in parts]


def glue(parts):
    """Transforms the list of sublists back into a new string
    
    Returns: string
    """
    return part_to_str([part_to_str(part) for part in parts])


def encrypt(sentence):
    """Reverses all consecutive letter parts in a string.
    
    Input: a string
    Returns: a string
    """
    parts = split_in_parts(sentence)
    return glue(reverse_relevant_parts(parts))


if __name__ == "__main__":

    paragraph = "toN ylno si ti ysae ot eil htiw spam, ti's laitnesse. oT yartrop lufgninaem spihsnoitaler rof a xelpmoc, eerht-lanoisnemid dlrow no a talf teehs fo repap ro a oediv neercs, a pam tsum trotsid ytilaer. sA a elacs ledom, eht pam tsum esu slobmys taht tsomla syawla era yllanoitroporp hcum reggib ro rekciht naht eht serutaef yeht tneserper. oT diova gnidih lacitirc noitamrofni ni a gof fo liated, eht pam tsum reffo a evitceles, etelpmocni weiv fo ytilaer. erehT's on epacse morf eht cihpargotrac xodarap: ot tneserp a lufesu dna lufhturht erutcip, na etarucca pam tsum llet etihw seil. --- woH ot eil htiw spam, kraM reinomnoM, 1996."
    print(encrypt(paragraph))
    assert encrypt(encrypt(paragraph)) == paragraph
