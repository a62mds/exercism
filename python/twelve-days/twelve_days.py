_days = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth',
         'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']

_phrases = ['a Partridge in a Pear Tree.\n',
            'two Turtle Doves, ',
            'three French Hens, ',
            'four Calling Birds, ',
            'five Gold Rings, ',
            'six Geese-a-Laying, ',
            'seven Swans-a-Swimming, ',
            'eight Maids-a-Milking, ',
            'nine Ladies Dancing, ',
            'ten Lords-a-Leaping, ',
            'eleven Pipers Piping, ',
            'twelve Drummers Drumming, ']

def verse(n):
    if not 1 <= n <= len(_phrases):
        raise IndexError('Song only has {} verses'.format(len(_phrases)))
    v = 'On the {} day of Christmas my true love gave to me, '.format(_days[n-1])
    for m in range(n-1, 0, -1):
        v += _phrases[m]
    last_phrase = 'and ' + _phrases[0] if n > 1 else _phrases[0]
    return v + last_phrase

def verses(start, end):
    return '\n'.join(verse(n) for n in range(start, end+1)) + '\n'

def sing():
    return verses(1, 12)
