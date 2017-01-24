import re


class Phone(object):
    def __init__(self, raw_num):
        self.number = raw_num
    @property
    def number(self):
        return self._number
    @number.setter
    def number(self, n):
        phnum_pattern = re.compile(r'^1?(\d{10})$')
        phnum = phnum_pattern.match(re.sub(r'[^\d]', '', n))
        self._number = phnum.group(1) if phnum is not None else '0'*10
    def area_code(self):
        return self.number[:3]
    def pretty(self):
        area_code = self.number[:3]
        central_office_code = self.number[3:6]
        station_code = self.number[6:]
        return '({0}) {1}-{2}'.format(area_code, central_office_code, station_code)

if __name__ == '__main__':
    def print_numbers(phone_number):
        def print_number(name, phone_number):
            print(name+' : {}'.format(phone_number))
        p = Phone(phone_number)
        print('='*(max(len(p.pretty()), len(phone_number))+15))
        print_number('input    ', phone_number)
        print_number('ph num   ', p.number)
        print_number('area code', p.area_code())
        print_number('formatted', p.pretty())
    valid_number = '11234567890'
    print_numbers(valid_number)
    invalid_number = '123456789'
    print_numbers(invalid_number)
    invalid_number2 = '21234567890'
    print_numbers(invalid_number2)
    dotted_number = '123.456.7890'
    print_numbers(dotted_number)
    formatted_number = '(123) 456-7890'
    print_numbers(formatted_number)
