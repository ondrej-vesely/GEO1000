a = '52496'
b = ''
c = '52-49.6'

def translate(string, delimiter='-'):
    words = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
    return delimiter.join([words[int(c)] for c in string if c.isdigit()])

print(translate(c))

