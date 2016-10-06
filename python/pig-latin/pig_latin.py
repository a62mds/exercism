from string import ascii_lowercase as alphabet


consonants = filter(lambda ll: ll not in 'aeiou', alphabet)

def translate(wordstr):
    return ' '.join(map(convert, wordstr.split()))

def convert(word):
    if word.startswith(('sch', 'squ', 'thr')):
        return word[3:] + word[0:3] + 'ay'
    elif word.startswith(('qu', 'ch', 'th')):
        return word[2:] + word[0:2] + 'ay'
    elif word.startswith(('yt', 'xr')):
        return word + 'ay'
    elif word[0] in consonants:
        return word[1:] + word[0] + 'ay'
    else:
        return word + 'ay'
