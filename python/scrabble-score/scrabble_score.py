letter_groups = {'aeioulnrst' : 1,
                 'dg' : 2,
                 'bcmp' : 3,
                 'fhvwy' : 4,
                 'k' : 5,
                 'jx' : 8,
                 'qz' : 10}

pts = {ltr : numpts for grp, numpts in letter_groups.iteritems() for ltr in grp}

def score(word):
    has_only_alpha = lambda w: all(l.isalpha() for l in w)
    return sum(pts[l] for l in word.lower()) if has_only_alpha(word) else 0
