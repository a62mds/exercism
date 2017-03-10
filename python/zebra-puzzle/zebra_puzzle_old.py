from itertools import product


class House(object):
    def __init__(self, pos=None, clr=None, nat=None, drk=None, smk=None, pet=None):
        self.position = pos
        self.color = clr
        self.nationality = nat
        self.drink = drk
        self.smoke = smk
        self.pet = pet

def univariate_clues(h):
    c2 = h.color == 'red' if h.nationality == 'Englishman' else True
    c3 = h.pet == 'dog' if h.nationality == 'Spaniard' else True
    c4 = h.drink == 'coffee' if h.color == 'green' else True
    c5 = h.drink == 'tea' if h.nationality == 'Ukranian' else True
    c7 = h.pet == 'snails' if h.smoke == 'Old Gold' else True
    c8 = h.smoke == 'Kools' if h.color == 'yellow' else True
    c9 = h.drink == 'milk' if h.position == 3 else True
    c10 = h.position == 0 if h.nationality == 'Norwegian' else True
    c13 = h.drink == 'orange juice' if h.smoke == 'Lucky Strike' else True
    c14 = h.smoke == 'Parliaments' if h.nationality == 'Japanese' else True
    return all([c2, c3, c4, c5, c7, c8, c9, c10, c13, c14])

def bivariate_clues(h1, h2):
    c6 = h2.position - h1.position == 1 if h1.color == 'green' and h2.color == 'ivory' else True
    c11 = abs(h2.position - h1.position) == 1 if h1.smoke == 'Chesterfields' and h2.pet == 'fox' else True
    c12 = abs(h2.position - h1.position) == 1 if h1.smoke == 'Kools' and h2.pet == 'horse' else True
    c15 = abs(h2.position - h1.position) == 1 if h1.nationality == 'Norwegian' and h2.color == 'blue' else True
    return all([c6, c11, c12, c15])

def solution():
    positions = range(5)
    colors = 'red green yellow ivory blue'.split()
    nationalities = 'Englishman Spaniard Ukranian Norwegian Japanese'.split()
    drinks = 'coffee, tea, milk, orange juice, water'.split(', ')
    smokes = 'Old Gold, Kools, Lucky Strike, Chesterfields, Parliaments'.split(', ')
    pets = 'dog snails fox horse zebra'.split()
    all_possibilities = product(positions, colors, nationalities, drinks, smokes, pets)
    all_houses = [House(pos=p[0], clr=p[1], nat=p[2], drk=p[3], smk=p[4], pet=p[5]) for p in all_possibilities]
    soln = filter(univariate_clues, all_houses)
    print(len(soln))
    for h1 in soln:
        for h2 in [h for h in soln if h != h1]:
            if not bivariate_clues(h1, h2):
                soln.remove(h2)
    print len(soln)
    def is_solution(h):
        p1 = h.position == 0
        p2 = h.color == 'yellow'
        p3 = h.nationality == 'Norwegian'
        p4 = h.drink == 'water'
        p5 = h.pet == 'zebra'
        return p1 and p2 and p3 and p4 and p5
    print any(is_solution(h) for h in soln)


if __name__ == '__main__':
    solution()
