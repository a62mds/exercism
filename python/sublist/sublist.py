
SUBLIST = 'sub'
SUPERLIST = 'spr'
EQUAL = 'eql'
UNEQUAL = 'neq'

def is_sublist(lst1, lst2):
    if not lst1:
        return True
    elif 0 < len(lst1) <= len(lst2):
        return any(lst1 == lst2[ii:ii+len(lst1)] for ii in range(len(lst2)-len(lst1)+1))
    else:
        return False

def is_superlist(lst1, lst2):
    return is_sublist(lst2, lst1)

def check_lists(lst1, lst2):
    if is_sublist(lst1, lst2) and not is_superlist(lst1, lst2):
        return SUBLIST
    elif is_superlist(lst1, lst2) and not is_sublist(lst1, lst2):
        return SUPERLIST
    elif is_sublist(lst1, lst2) and is_superlist(lst1, lst2):
        return EQUAL
    else:
        return UNEQUAL
