#!/usr/bin/env python
from collections import namedtuple
from itertools import product


def conjoin(*predicates):
    def conjoined(x):
        for predicate in predicates:
            if not predicate(x): return False
        return True
    return conjoined


HouseProperty = namedtuple('HouseProperty', ['name', 'value'])


class House(object):

    _positions = list(range(5))
    _colors = 'red green yellow ivory blue'.split()
    _nats = 'Englishman Spaniard Ukranian Norwegian Japanese'.split()
    _drinks = 'coffee, tea, milk, orange juice, water'.split(', ')
    _smokes = 'Old Gold, Kools, Lucky Strike, Chesterfields, Parliaments'.split(', ')
    _pets = 'dog snails fox horse zebra'.split()

    @classmethod
    def list_properties(cls):
        return [cls._positions,
                cls._colors,
                cls._nats,
                cls._drinks,
                cls._smokes,
                cls._pets]

    @classmethod
    def all_possibilities(cls):
        return product(*cls.list_properties())

    def __init__(self, pos, clr, nat, drk, smk, pet):
        self.position = pos
        self.color = clr
        self.nat = nat
        self.drink = drk
        self.smoke = smk
        self.pet = pet
        self.properties = (self.position, self.color, self.nat, self.drink, self.smoke, self.pet)

    def __str__(self):
        return ', '.join(map(str, self.properties))

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, clr):
        if clr in self._colors: self._color = clr
        else: raise ValueError('{} not a valid color'.format(clr))

    @property
    def nat(self):
        return self._nat

    @nat.setter
    def nat(self, nat):
        if nat in self._nats: self._nat = nat
        else: raise ValueError('{} not a valid nat'.format(nat))

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

    def is_right_of(self, other):
        return self.position == other.position + 1

    def is_left_of(self, other):
        return other.position == self.position + 1

    def is_nbr_of(self, other):
        return self.is_right_of(other) or self.is_left_of(other)


class ZebraPuzzle(object):

    def __init__(self):
        self.houses = (House(*h) for h in House.all_possibilities())

    def unary_constraint(self, h, prop1, prop2):
        if getattr(h, prop1.name) == prop1.value:
            return getattr(h, prop2.name) == prop2.value
        elif getattr(h, prop2.name) == prop2.value:
            return getattr(h, prop1.name) == prop1.value
        else:
            return True

    def binary_constraint(self, h, pname1, pvalue1, pname2, pvalue2, posrel):
        if getattr(h, pname1) == pvalue1 and getattr(h, pname2) == pvalue2:
            return False
        elif getattr(h, pname1) == pvalue1:
            return any(getattr(hh, pname2) == pvalue2 for hh in
                       filter(lambda hhh: getattr(h, posrel)(hhh), self.houses))
        elif getattr(h, pname2) == pvalue2:
            return any(getattr(hh, pname1) == pvalue1 for hh in
                       filter(lambda hhh: getattr(hhh, posrel)(h), self.houses))
        else:
            return True

    # Clue 1: There are five houses.

    # Clue 2: The Englishman lives in the red house
    def englishman_in_red_house(self, h):
        occupied_by_englishman = HouseProperty(name='nat', value='Englishman')
        colored_red = HouseProperty(name='color', value='red')
        return self.unary_constraint(h, occupied_by_englishman, colored_red)

    # Clue 3: The Spaniard owns the dog
    def spaniard_owns_dog(self, h):
        occupied_by_spaniard = HouseProperty(name='nat', value='Spaniard')
        keeps_pet_dog = HouseProperty(name='pet', value='dog')
        return self.unary_constraint(h, occupied_by_spaniard, keeps_pet_dog)

    # Clue 4: Coffee is drunk in the green house
    def coffee_in_green_house(self, h):
        drinks_coffee = HouseProperty(name='drink', value='coffee')
        colored_green = HouseProperty(name='color', value='green')
        return self.unary_constraint(h, drinks_coffee, colored_green)

    # Clue 5: The Ukranian drinks tea
    def ukranian_drinks_tea(self, h):
        occupied_by_ukranian = HouseProperty(name='nat', value='Ukranian')
        drinks_tea = HouseProperty(name='drink', value='tea')
        return self.unary_constraint(h, occupied_by_ukranian, drinks_tea)

    # Clue 6: The green house is immediately to the right of the ivory house
    def green_house_is_right_of_ivory_house(self, h):
        return self.binary_constraint(h, 'color', 'green', 'color', 'ivory', 'is_right_of')

    # Clue 7: The Old Gold smoker owns snails
    def old_gold_smoker_owns_snails(self, h):
        smokes_old_gold = HouseProperty(name='smoke', value='Old Gold')
        keeps_pet_snails = HouseProperty(name='pet', value='snails')
        return self.unary_constraint(h, smokes_old_gold, keeps_pet_snails)

    # Clue 8: Kools are smoked in the yellow house
    def kools_smoker_in_yellow_house(self, h):
        smokes_kools = HouseProperty(name='smoke', value='Kools')
        colored_yellow = HouseProperty(name='color', value='yellow')
        return self.unary_constraint(h, smokes_kools, colored_yellow)

    # Clue 9: Milk is drunk in the middle house
    def milk_in_middle_house(self, h):
        is_in_middle = HouseProperty(name='position', value=2)
        drinks_milk = HouseProperty(name='drink', value='milk')
        return self.unary_constraint(h, is_in_middle, drinks_milk)

    # Clue 10: The Norwegian lives in the first house
    def norwegian_in_leftmost_house(self, h):
        occupied_by_norwegian = HouseProperty(name='nat', value='Norwegian')
        is_first_house = HouseProperty(name='position', value=0)
        return self.unary_constraint(h, occupied_by_norwegian, is_first_house)

    # Clue 11: The man who smokes Chesterfields lives in the house next to the man with the fox
    def chester_smoker_next_to_fox_keeper(self, h):
        return self.binary_constraint(h, 'smoke', 'Chesterfields', 'pet', 'fox', 'is_nbr_of')

    # Clue 12: Kools are smoked in the house next to the house where the horse is kept
    def kools_smoker_next_to_horse_keeper(self, h):
        return self.binary_constraint(h, 'smoke', 'Kools', 'pet', 'horse', 'is_nbr_of')

    # Clue 13: The Lucky Strike smoker drinks orange juice
    def lucky_strike_smoker_drinks_orange_juice(self, h):
        smokes_lucky_strike = HouseProperty(name='smoke', value='Lucky Strike')
        drinks_orange_juice = HouseProperty(name='drink', value='orange juice')
        return self.unary_constraint(h, smokes_lucky_strike, drinks_orange_juice)

    # Clue 14: The Japanese smokes Parliaments
    def japanese_smokes_parliaments(self, h):
        occupied_by_japanese = HouseProperty(name='nat', value='Japanese')
        smokes_parliaments = HouseProperty(name='smoke', value='Parliaments')
        return self.unary_constraint(h, occupied_by_japanese, smokes_parliaments)

    # Clue 15: The Norwegian lives next to the blue house
    def norwegian_next_to_blue_house(self, h):
        is_second_house = HouseProperty(name='position', value=1)
        colored_blue = HouseProperty(name='color', value='blue')
        return self.unary_constraint(h, is_second_house, colored_blue)

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
            nats_at_p = set(h.nat for h in houses_at_p)
            if len(nats_at_p) == 1:
                n = list(nats_at_p)[0]
                houses_not_n = filter(lambda h: h.nat != n, self.houses)
                self.houses = sorted(houses_at_p + houses_not_n, key=lambda h:h.position)

    @property
    def unary_constraints(self):
        return [self.englishman_in_red_house,
                self.spaniard_owns_dog,
                self.coffee_in_green_house,
                self.ukranian_drinks_tea,
                self.old_gold_smoker_owns_snails,
                self.kools_smoker_in_yellow_house,
                self.milk_in_middle_house,
                self.norwegian_in_leftmost_house,
                self.lucky_strike_smoker_drinks_orange_juice,
                self.japanese_smokes_parliaments,
                self.norwegian_next_to_blue_house]

    @property
    def binary_constraints(self):
        return [self.green_house_is_right_of_ivory_house,
                self.kools_smoker_next_to_horse_keeper,
                self.chester_smoker_next_to_fox_keeper]

    def solve(self):
        self.houses = filter(conjoin(*self.unary_constraints), self.houses)
        """
        for bc in self.binary_constraints:
            self.houses = filter(bc, self.houses)
            self.uniqueness_constraint()
        """
        self.houses = filter(self.green_house_is_right_of_ivory_house, self.houses)
        self.uniqueness_constraint()
        self.houses = filter(self.kools_smoker_next_to_horse_keeper, self.houses)
        self.uniqueness_constraint()
        self.houses = filter(self.chester_smoker_next_to_fox_keeper, self.houses)
        self.uniqueness_constraint()
        for h in self.houses:
            print(h)
        print(len(self.houses))


def solution():
    zp = ZebraPuzzle()
    zp.solve()
    """
    water_house = filter(lambda h: h.drink == 'water', zp.houses)
    zebra_house = filter(lambda h: h.pet == 'zebra', zp.houses)
    if not len(water_house) == 1 or not len(zebra_house) == 1:
        raise RuntimeError("Unique solution not found")
    else:
        water_house = water_house[0]
        zebra_house = zebra_house[0]
        wstr = "It is the {} who drinks the water.".format(water_house.nat)
        zstr = "The {} keeps the zebra.".format(zebra_house.nat)
        return '\n'.join([wstr, zstr])
    """

if __name__ == '__main__':
    print(solution())
