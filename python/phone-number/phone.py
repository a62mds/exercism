import re


class Phone(object):
    def __init__(self, raw_num, debugging=False):
        self.debugging = debugging
        self.number = raw_num
    @property
    def number(self):
        return self._number
    @number.setter
    def number(self, n):
        phnum_pattern = re.compile(r'^1(\d{10})$')
        phnum = phnum_pattern.match(n)
        if phnum is not None:
            self._number = phnum.group(1)
            ###
            # Debugging mode:
            if self.debugging: print('self._number : {}'.format(self._number))
            ###
        else:
            num_str = 'Invalid phone number: {}'.format(n)
            ###
            # Debugging mode:
            if self.debugging: print(num_str)
            ###
            else: raise ValueError(num_str)
    @property
    def debugging(self):
        return self._debugging
    @debugging.setter
    def debugging(self, d):
        self._debugging = d if d == True else False
    def area_code(self):
        return self.number[:3]
    def pretty(self):
        area_code = self.number[:3]
        central_office_code = self.number[3:6]
        station_code = self.number[6:]
        return '({0}) {1}-{2}'.format(area_code, central_office_code, station_code)

if __name__ == '__main__':
    valid_number = '11234567890'
    valid_phone = Phone(valid_number, debugging=True)
    print(valid_phone.area_code())
    print(valid_phone.pretty())
    invalid_number = '123456789'
    invalid_phone = Phone(invalid_number, debugging=True)
