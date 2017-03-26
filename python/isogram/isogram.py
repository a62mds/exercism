from string import ascii_lowercase as abcs


def fold_right(op, seq, acc):
    if len(seq) == 0:
        return acc
    else:
        return fold_right(op, seq[1:], op(acc, seq[0]))

def is_isogram(text):
    if text == '': return True
    text = filter(lambda c: c in abcs, map(lambda c: c.lower(), text))
    used_letters = fold_right(lambda ls, l: ls + [l] if l not in ls else [], text, [])
    return len(text) == len(used_letters)
