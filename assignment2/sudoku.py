# GEO1000 - Assignment 2
# Authors: Ondrej Vesely, Giorgos Triantafyllou
# Studentnumbers: 5162130, 5381738


_bitmasks = [
    # rows
    '1111000000000000',
    '0000111100000000',
    '0000000011110000',
    '0000000000001111',
    # columns
    '1000'*4,
    '0100'*4,
    '0010'*4,
    '0001'*4,
    # cells
    '1100110000000000',
    '0011001100000000',
    '0000000011001100',
    '0000000000110011']


def parse(sudoku):
    if len(sudoku) == 16 and sudoku.isdigit():
        return [tuple([int(n) for n, bit in zip(sudoku, mask) if int(bit)]) for mask in _bitmasks]


def is_valid(structure):
    test = [1,2,3,4]
    for chunk in structure:
        for number in test:
            if not number in chunk:
                return False
    return True


def main():
    sudoku = input('Your sudoku for validation, or "quit" to exit:  ')

    if sudoku == 'quit':
        pass
    
    else:
        chunks = parse(sudoku)
        if not chunks:
            print('Input not understood.')      
        else:
            # print out the sudoku because its nice
            print('\n'.join(['  '.join([str(n) for n in ch]) for ch in chunks[:4]]))
            print('This sudoku is %s' % ('*INVALID*', '*VALID*')[is_valid(chunks)])
            
        main()


if __name__ == "__main__":
    main()
    
