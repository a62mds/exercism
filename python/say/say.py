#!/usr/bin/env python

####
# Stuff for ensuring numbers are within a specified range (overkill, but
# whatever :-)
open_range_test   = lambda num, lbnd, ubnd: lbnd <  num <  ubnd
clopen_range_test = lambda num, lbnd, ubnd: lbnd <= num <  ubnd
opesed_range_test = lambda num, lbnd, ubnd: lbnd <  num <= ubnd
closed_range_test = lambda num, lbnd, ubnd: lbnd <= num <= ubnd

is_in_range = {'()' : open_range_test,
               '[)' : clopen_range_test,
               '(]' : opesed_range_test,
               '[]' : closed_range_test}

class RangeError(AttributeError):
    def __init__(self, lbnd, ubnd):
        self.emsg = 'Number not in range [{0}, {1})'.format(lbnd, ubnd)
        AttributeError.__init__(self, self.emsg)

####
# English names of numbers and number groups
thousands = ['billion', 'million', 'thousand', '']
tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty',
        'sixty', 'seventy', 'eighty', 'ninety']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
         'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
ones = ['', 'one', 'two', 'three', 'four',
        'five', 'six', 'seven', 'eight', 'nine']

####
# splits a number into a list of its digits
#   -> e.g.: 837 => [8, 3, 7]
group_by_ones = lambda num: [int(d) for d in str(num)]
# splits a number every three decimal places from the right (i.e. into
# thousands; e.g.: 9837485867 => 9,837,485,867 => [9, 837, 485, 867])
to_int = lambda n: int(float(n))
group_by_thousands = lambda num: map(to_int, '{0:,}'.format(num).split(','))

####
# Translate two digit numbers to English
def name_tens(num):
    # Guarantee num is a two digit number
    lbnd = 0
    ubnd = 100
    if not is_in_range['[)'](num, lbnd, ubnd):
        raise RangeError(lbnd, ubnd)
    # split num into its digits and pad left with a zero if num is a single
    # digit number
    digits = group_by_ones(num)
    digits = [0]*(2-len(digits)) + digits
    # if num is single digit
    if not digits[0]:
        return ones[digits[1]]
    # if num is in the teens
    elif digits[0] == 1:
        return teens[digits[1]]
    else:
        if not digits[1]:
            return tens[digits[0]]
        else:
            return tens[digits[0]] + '-' + ones[digits[1]]

def name_hundreds(num):
    # Guarantee num is a three digit number
    lbnd = 0
    ubnd = 1000
    if not is_in_range['[)'](num, lbnd, ubnd):
        raise RangeError(lbnd, ubnd)
    # split num into its digits and pad left with zeros if necessary
    #   -> e.g.:   7 => [0, 0, 7]
    #             37 => [0, 3, 7]
    digits = group_by_ones(num)
    digits = [0]*(3-len(digits)) + digits
    #
    if not digits[0]:
        return name_tens(int(''.join(map(str, digits[1:]))))
    elif not any(digits[1:]):
        return ones[digits[0]] + ' hundred'
    else:
        return ones[digits[0]]+' hundred and '+name_tens(int(''.join(map(str, digits[1:]))))

def say(num):
    # Guarantee num is in range 0 <= num <= 999,999,999,999
    lbnd = 0
    ubnd = 1000000000000
    if not is_in_range['[)'](num, lbnd, ubnd):
        raise RangeError(lbnd, ubnd)
    # Treat zero as a special case
    if not num:
        return 'zero'
    # For use concatenating the English versions of the numbers composing the
    # thousands groups appropriately
    #   -> e.g.: 843,342 => [('eight hundred and forty-three', 'thousand'),
    #                        ('three hundred and forty-two', '')]
    #                    => 'eight hundred and forty-three thousand \
    #                        three hundred and forty-two'
    cct = lambda (str1, str2): str1 + ' ' + str2 if str1 else ''
    # Gets the English names of the groups of thousands
    #   -> e.g.: [843, 342] => ['eight hundred and forty-three',
    #                           'three hundred and forty-two']
    translate_groups_of = lambda n: map(name_hundreds, group_by_thousands(n))
    # Matches each English-translated group with its English group name
    #   -> e.g.: gs = [g1, g2,..., gN], ns = [n1, n2,..., nN]
    #            gs, ns => [(g1, n1), (g2, n2),..., (gN, nN)]
    # - note: zip 'zips' iterables from left to right; if one of the iterables
    #         is shorter, zipping ignores the 'extra' elements in the longer
    #         iterable; the reversing ensures that the zipping occurs in this
    #         case from right to left
    #           -> there must be a better way...should look
    match_group_names = lambda gs, ns: reversed(zip(reversed(gs), reversed(ns)))
    # Formats the final string properly by removing any trailing whitespace and
    # replacing any double spaces with the word 'and'
    # - note: replacing '  ' by ' and ' will NOT work in general; should
    #         investigate and find actual solution
    fmt = lambda rawstr: rawstr.rstrip().replace('  ', ' and ')
    return fmt(' '.join(map(cct, match_group_names(translate_groups_of(num), thousands))))
