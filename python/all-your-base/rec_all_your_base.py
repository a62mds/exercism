# Recursive version

def check_validity(old_base, digits, new_base):
    for d in digits:
        if not d in range(old_base): raise ValueError('Invalid digit: {}'.format(d))
    if old_base < 2: raise ValueError('Invalid base: {}'.format(old_base))
    elif new_base < 2: raise ValueError('Invalid base: {}'.format(new_base))
    else: pass

def rec_to_base10(old_base, digits):
    def rec(digits, acc, ind):
        if len(digits) == 0: return acc
        else: return rec(digits[:-1], acc+digits[-1]*pow(old_base, ind), ind+1)
    return rec(digits, 0, 0)

def rec_fr_base10(new_base, num):
    def rec(num, acc):
        if num == 0: return acc
        else: return rec(num//new_base, [num%new_base]+acc)
    return rec(num, [])

def rebase(old_base, digits, new_base):
    check_validity(old_base, digits, new_base)
    return rec_fr_base10(new_base, rec_to_base10(old_base, digits))
