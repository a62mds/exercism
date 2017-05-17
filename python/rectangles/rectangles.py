CORNER = '+'
VSIDE = '|'
SIDES = [CORNER, VSIDE]


def count(ascii_diagram=[]):
    _count = 0
    for lnum1, line1 in enumerate(ascii_diagram):
        for cnum1, char1 in enumerate(line1):
            if char1 == CORNER:
                for cnum2, char2 in enumerate(line1[cnum1 + 1:]):
                    if char2 == CORNER:
                        for line2 in ascii_diagram[lnum1 + 1:]:
                            if line2[cnum1] == line2[cnum1 + cnum2 + 1] == CORNER:
                                _count += 1
                            elif line2[cnum1] in SIDES and line2[cnum1 + cnum2 + 1] in SIDES:
                                continue
                            else:
                                break
    return _count
