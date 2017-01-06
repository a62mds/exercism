from fractions import gcd
from math import sqrt


sq = lambda x: x * x
is_odd = lambda n: isinstance(n, int) and n % 2 != 0

ODD = 'odd'
EVEN = 'even'

def is_triplet(triple):
    # Following convention, a and b denote the lengths of the 'legs' of the
    # triangle and c denotes the length of the hypotenuse. This convention
    # requires that c > a and c > b (for nonzero a and b), hence the largest
    # value in the tuple argument "triple" should be assigned to c. How the
    # remaining values are assigned to the variables a and b does not affect the
    # whether or not (a, b, c) forms a Pythagorean triple, hence the following:
    a, b, c = sorted(triple)
    return sq(a) + sq(b) == sq(c)

def satisfies_criteria(m, n):
    # Ensure m and n satisfy the necessary criteria for use in Euclid's formula
    are_in_range = m > n > 0
    are_coprime = gcd(m, n) == 1
    have_different_parity = is_odd(m) != is_odd(n)
    return are_in_range and are_coprime and have_different_parity

def gen_triplets(b):
    # From Euclid's formula, given coprime integers m, n with m > n > 0, the
    # triple (m^2 - n^2, 2mn, m^2 + n^2) is a primitive Pythagorean triple,
    # provided m and n are not both odd. In this case, m^2 - n^2 is odd, while
    # 2mn is even (as it always is). Thus, if the argument b is odd, let
    # b = m^2 - n^2 and let a = 2mn; otoh, if b is even, let a = m^2 - n^2 and
    # let b = 2mn
    parity_of = lambda b: ODD if is_odd(b) else EVEN
    pick_a_using = {EVEN : lambda m, n: sq(m) - sq(n),
                    ODD  : lambda m, n: 2 * m * n}
    a = pick_a_using[parity_of(b)]
    # Given b and picking any m, solve the relevant equation to find n
    pick_n_using = {EVEN : lambda b, m: b / (2 * m),
                    ODD  : lambda b, m: sqrt(sq(m) - b)}
    n = pick_n_using[parity_of(b)]
    # Formula for c is always m^2 + n^2
    c = lambda m, n: sq(m) + sq(n)
    # Generates primitive pythagorean triplets
    for mm in range(1, b):
        nn = n(b, mm)
        aa = a(mm, nn)
        # Imposes the condition aa < bb so that each yielded triplet is ordered
        # from smallest to largest, as per test specs
        aa, bb = (b, aa) if aa > b else (aa, b)
        cc = c(mm, nn)
        if satisfies_criteria(mm, nn) and is_triplet((aa, bb, cc)):
            yield (aa, bb, cc)

# This seems wasteful and needs work
def gen_triplets_in_range(min, max):
    for bb in range(min, max):
        for aa in range(min, bb):
            cc = int(sqrt(sq(aa) + sq(bb)))
            if cc <= max and is_triplet((aa, bb, cc)):
                yield (aa, bb, cc)

def primitive_triplets(b):
    return set(gen_triplets(b))

def triplets_in_range(min, max):
    return set(gen_triplets_in_range(min, max))
