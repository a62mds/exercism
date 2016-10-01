
roman = {1 : 'I',
         5 : 'V',
         10 : 'X',
         50 : 'L',
         100 : 'C',
         500 : 'D',
         1000 : 'M'}

def to_roman(digits):
    numerals = ['' if not digits[0] else 'M'*digits[0]]
    for ii in [1, 2, 3]:
        tens_place = 3 - ii
        if not digits[ii]:
            numerals.append('')
        elif 1 <= digits[ii] <= 3:
            numerals.append(roman[10**tens_place] * digits[ii])
        elif digits[ii] == 4:
            numerals.append(roman[10**tens_place] + roman[5 * 10**tens_place])
        elif 5 <= digits[ii] <= 8:
            numerals.append(roman[5 * 10**tens_place] +
                            roman[10**tens_place] * (digits[ii] - 5))
        elif digits[ii] == 9:
            numerals.append(roman[10**tens_place] + roman[10 * 10**tens_place])
        else:
            raise ValueError('Anomaly encountered')
    return numerals

def numeral(number):
    if not 1 <= number <= 3000:
        raise ValueError('Number out of range')
    digits = [0] * (4-len(str(number))) + [int(d) for d in str(number)]
    return ''.join(to_roman(digits))
