def foldl(op, seq, acc):
    assert(isinstance(seq, (list, str, tuple)))
    return op(seq[0], acc) if len(seq) == 1 else foldl(op, seq[:-1], op(seq[-1], acc))

def check_validity(old_base, digits, new_base):
    for d in digits:
        if not d in range(old_base): raise ValueError('Invalid digit: {}'.format(d))
    if old_base < 2: raise ValueError('Invalid base: {}'.format(old_base))
    elif new_base < 2: raise ValueError('Invalid base: {}'.format(new_base))
    else: pass

def rec_to_base10(old_base, digits, acc):
    if len(digits) == 1:
        return digits[-1] * 10
    else:
        raise Exception('Not Implemented')

def rec_fr_base10(new_base, num):
    raise Exception('Not Implemented')
    acc = []
    while num > 0:
        acc = [num % new_base] + acc
        num = num // new_base
    return acc

def rebase(old_base, digits, new_base):
    check_validity(old_base, digits, new_base)
    return fr_base10(new_base, to_base10(old_base, digits))
