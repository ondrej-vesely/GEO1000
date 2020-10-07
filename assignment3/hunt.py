# GEO1000 - Assignment 3
# Authors: Ondrej Vesely, Giorgos Triantafyllou
# Studentnumbers: 5162130, 5381738

def read_grid(finite):
    """Parse the input text file into a nested list of <int>tuples."""
    nested_list = []
    with open(finite, 'r') as f:
        for row in f:
            row_list = row.split('|')
            row_list = [x.strip() for x in row_list]
            row_list = [(int(x[0]), int(x[1])) for x in row_list if x.isdigit()]
            if row_list:
                nested_list.append(row_list)
    return nested_list


def visit(table, steps_allowed, path):
    """Traverses the table for n of allowed steps
    Return True if self referencing cell was found.
    Records path into path.
    """
    prev = None
    visit = (0,0)
    for step in range(steps_allowed):
        if visit == prev:
            return True
        else:
            path.append(visit)
            prev = visit
            visit = table[visit[0]][visit[1]]
    return False


def hunt(filenm, max_steps):
    """Main function that hunts for treasure in provided file."""
    table = read_grid(filenm)
    path = []

    if visit(table, max_steps, path):
        row = path[-1][0]
        col = path[-1][1]
        msg = "The treasure was found at row: %s, column: %s; it took %s steps to find the treasure." % (row, col, len(path))
    else:
        msg = "Could not find a treasure (in %s steps)." % max_steps
    return msg


if __name__ == "__main__":
    print(hunt('finite.txt', 20))


   