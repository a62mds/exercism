class Luhn(object):
    def __init__(self, number):
        self.number = number
        self.digits = [int(d) for d in str(self.number)]
    def addends(self):
        # Returns 2 for every second digit from the right, and 1 for the rest
        factor = lambda ii: 2 if (len(self.digits)-ii)%2==0 else 1
        # Subtracts 9 if digit is greater than 9
        mk_single_dgt = lambda d: d if d <= 9 else d - 9
        # Create list of digits with appropriate ones doubled and map any two
        # digit numbers dd to dd - 9
        return map(mk_single_dgt, [factor(i)*d for i,d in enumerate(self.digits)])
    def checksum(self):
        return sum(self.addends())
    def is_valid(self):
        return self.checksum() % 10 == 0
    @staticmethod
    def create(number):
        chk_dgt = (Luhn(number * 10).checksum() * 9) % 10
        return number * 10 + chk_dgt
