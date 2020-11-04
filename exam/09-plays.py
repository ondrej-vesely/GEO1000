plays = {
    'artist A':
        {'track A': 10, 'track B': 11},
    'artist B':
        {'track C': 4, 'track D': 7},
}

sum(plays['artist A'].values())
plays['artist A']['track B'] += 1
plays['artist C'] = {'track E': 0}
plays.pop('artist C')
plays['artist B']['track D_NEW'] = plays['artist B'].pop('track D')

print(plays)