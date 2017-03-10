from itertools import product


def conjoin(*predicates):
    def conjoined(x):
        for predicate in predicates:
            if not predicate(x): return False
        return True
    return conjoined

def unary_constraint(prop1, prop2):
    if prop1: return prop2
    elif prop2: return prop1
    else: return True


class House(object):
    _positions = range(5)
    _colors = 'red green yellow ivory blue'.split()
    _nationalities = 'Englishman Spaniard Ukranian Norwegian Japanese'.split()
    _drinks = 'coffee, tea, milk, orange juice, water'.split(', ')
    _smokes = 'Old Gold, Kools, Lucky Strike, Chesterfields, Parliaments'.split(', ')
    _pets = 'dog snails fox horse zebra'.split()
    @classmethod
    def all_possibilities(cls):
        return product(cls._positions,
                       cls._colors,
                       cls._nationalities,
                       cls._drinks,
                       cls._smokes,
                       cls._pets)
    def __init__(self, pos, clr, nat, drk, smk, pet):
        self.position = pos
        self.color = clr
        self.nationality = nat
        self.drink = drk
        self.smoke = smk
        self.pet = pet
    def __str__(self):
        return '{}, {}, {}, {}, {}, {}'.format(self.position,
                                               self.color,
                                               self.nationality,
                                               self.drink,
                                               self.smoke,
                                               self.pet)
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, clr):
        if clr in self._colors: self._color = clr
        else: raise ValueError('{} not a valid color'.format(clr))
    @property
    def nationality(self):
        return self._nationality
    @nationality.setter
    def nationality(self, nat):
        if nat in self._nationalities: self._nationality = nat
        else: raise ValueError('{} not a valid nationality'.format(nat))
    @property
    def drink(self):
        return self._drink
    @drink.setter
    def drink(self, drk):
        if drk in self._drinks: self._drink = drk
        else: raise ValueError('{} not a valid drink'.format(drk))
    @property
    def smoke(self):
        return self._smoke
    @smoke.setter
    def smoke(self, smk):
        if smk in self._smokes: self._smoke = smk
        else: raise ValueError('{} not a valid smoke'.format(smk))
    @property
    def pet(self):
        return self._pet
    @pet.setter
    def pet(self, pet_):
        if pet_ in self._pets: self._pet = pet_
        else: raise ValueError('{} not a valid pet'.format(pet_))
    def to_right_of(self, other):
        return self.position == other.position + 1
    def to_left_of(self, other):
        return other.position == self.position + 1
    def is_nbr_of(self, other):
        return self.to_right_of(other) or self.to_left_of(other)


class ZebraPuzzle(object):
    def __init__(self):
        self.houses = (House(*h) for h in House.all_possibilities())
    def cons2(self, h):
        return unary_constraint(h.nationality == 'Englishman', h.color == 'red')
    def cons3(self, h):
        return unary_constraint(h.nationality == 'Spaniard', h.pet == 'dog')
    def cons4(self, h):
        return unary_constraint(h.color == 'green', h.drink == 'coffee')
    def cons5(self, h):
        return unary_constraint(h.nationality == 'Ukranian', h.drink == 'tea')
    def cons6(self, h):
        green_houses = filter(lambda h: h.color == 'green', self.houses)
        ivory_houses = filter(lambda h: h.color == 'ivory', self.houses)
        if h in green_houses:
            return any(h.to_right_of(ih) for ih in ivory_houses)
        elif h in ivory_houses:
            return any(h.to_left_of(gh) for gh in green_houses)
        else:
            return True
    def cons7(self, h):
        return unary_constraint(h.smoke == 'Old Gold', h.pet == 'snails')
    def cons8(self, h):
        return unary_constraint(h.smoke == 'Kools', h.color == 'yellow')
    def cons9(self, h):
        return unary_constraint(h.position == 2, h.drink == 'milk')
    def cons10(self, h):
        return unary_constraint(h.nationality == 'Norwegian', h.position == 0)
    def cons11(self, h):
        chester_smokers = filter(lambda h: h.smoke == 'Chesterfields', self.houses)
        houses_with_fox = filter(lambda h: h.pet == 'fox', self.houses)
        if h in chester_smokers and h in houses_with_fox:
            return False
        elif h in chester_smokers:
            return any(h.is_nbr_of(fh) for fh in houses_with_fox)
        elif h in houses_with_fox:
            return any(h.is_nbr_of(ch) for ch in chester_smokers)
        else:
            return True
    def cons12(self, h):
        kools_smokers = filter(lambda h: h.smoke == 'Kools', self.houses)
        horse_keepers = filter(lambda h: h.pet == 'horse', self.houses)
        if h in kools_smokers and h in horse_keepers:
            return False
        elif h in kools_smokers:
            return any(h.is_nbr_of(hh) for hh in horse_keepers)
        elif h in horse_keepers:
            return any(h.is_nbr_of(kh) for kh in kools_smokers)
        else:
            return True
    def cons13(self, h):
        return unary_constraint(h.smoke == 'Lucky Strike', h.drink == 'orange juice')
    def cons14(self, h):
        return unary_constraint(h.nationality == 'Japanese', h.smoke == 'Parliaments')
    def cons15(self, h):
        norwegians = filter(lambda h: h.nationality == 'Norwegian', self.houses)
        blue_houses = filter(lambda h: h.color == 'blue', self.houses)
        if h in norwegians:
            return not h in blue_houses
        elif h in blue_houses:
            return all(h.to_right_of(nh) for nh in norwegians)
        else:
            return not any(h.to_right_of(nh) for nh in norwegians)
    def uniqueness_constraint(self):
        for p in range(5):
            houses_at_p = filter(lambda h: h.position == p, self.houses)
            houses_not_at_p = [h for h in self.houses if h not in houses_at_p]
            colors_at_p = set(h.color for h in houses_at_p)
            if len(colors_at_p) == 1:
                c = list(colors_at_p)[0]
                houses_not_c = filter(lambda h: h.color != c, self.houses)
                self.houses = sorted(houses_at_p + houses_not_c, key=lambda h:h.position)
            drinks_at_p = set(h.drink for h in houses_at_p)
            if len(drinks_at_p) == 1:
                d = list(drinks_at_p)[0]
                houses_not_d = filter(lambda h: h.drink != d, self.houses)
                self.houses = sorted(houses_at_p + houses_not_d, key=lambda h:h.position)
            smokes_at_p = set(h.smoke for h in houses_at_p)
            if len(smokes_at_p) == 1:
                s = list(smokes_at_p)[0]
                houses_not_s = filter(lambda h: h.smoke != s, self.houses)
                self.houses = sorted(houses_at_p + houses_not_s, key=lambda h:h.position)
            for pet in House._pets:
                if not any(h.pet == pet for h in houses_not_at_p):
                    houses_at_p = filter(lambda h: h.pet == pet, houses_at_p)
                    self.houses = sorted(houses_at_p + houses_not_at_p, key=lambda h:h.position)
            nats_at_p = set(h.nationality for h in houses_at_p)
            if len(nats_at_p) == 1:
                n = list(nats_at_p)[0]
                houses_not_n = filter(lambda h: h.nationality != n, self.houses)
                self.houses = sorted(houses_at_p + houses_not_n, key=lambda h:h.position)
    def solve(self):
        unary_constraints = [self.cons2, self.cons3, self.cons4, self.cons5,
                             self.cons7, self.cons8, self.cons9, self.cons10,
                             self.cons13, self.cons14]
        binary_constraints = [self.cons15, self.cons6, self.cons12, self.cons11]
        self.houses = filter(conjoin(*unary_constraints), self.houses)
        for bc in binary_constraints:
            self.houses = filter(bc, self.houses)
            self.uniqueness_constraint()


def solution():
    zp = ZebraPuzzle()
    zp.solve()
    zebra_house = filter(lambda h: h.pet == 'zebra', zp.houses)
    water_house = filter(lambda h: h.drink == 'water', zp.houses)
    if not len(zebra_house) == 1 or not len(water_house) == 1:
        raise RuntimeError("Unique solution not found")
    else:
        wstr = "It is the {} who drinks the water.".format(water_house[0].nationality)
        zstr = "The {} keeps the zebra.".format(zebra_house[0].nationality)
        return '\n'.join([wstr, zstr])

if __name__ == '__main__':
    print(solution())
