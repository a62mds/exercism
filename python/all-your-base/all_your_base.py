def check_validity(old_base, digits, new_base):
    for d in digits:
        if not d in range(old_base): raise ValueError('Invalid digit: {}'.format(d))
    if old_base < 2: raise ValueError('Invalid base: {}'.format(old_base))
    elif new_base < 2: raise ValueError('Invalid base: {}'.format(new_base))
    else: pass

def to_base10(old_base, digits):
    acc = 0
    ii = 0
    for d in digits[::-1]:
        acc += d*pow(old_base, ii)
        ii += 1
    return acc

def fr_base10(new_base, num):
    acc = []
    while num > 0:
        acc = [num % new_base] + acc
        num = num // new_base
    return acc

def rebase(old_base, digits, new_base):
    check_validity(old_base, digits, new_base)
    return fr_base10(new_base, to_base10(old_base, digits))
