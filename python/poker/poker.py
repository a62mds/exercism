class PlayingCard(object):
    _ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    _suits = 'C D H S'.split()
    def __init__(self, card):
        self.rank = card[:-1]
        self.suit = card[-1]
    @property
    def rank(self):
        return self._rank
    @rank.setter
    def rank(self, r):
        if r in self._ranks or r == 'T':
            self._rank = r
        else:
            raise ValueError('Invalid card rank: {}'.format(r))
    @property
    def suit(self):
        return self._suit
    @suit.setter
    def suit(self, s):
        if s in PlayingCard._suits:
            self._suit = s
        else:
            raise ValueError('Invalid card suit: {}'.format(s))
    @property
    def num_ranking(self):
        rank = '10' if self.rank == 'T' else self.rank
        return self._ranks.index(rank)
    def __str__(self):
        return ''.join([self.rank, self.suit])
    def __eq__(self, other):
        return self.rank == other.rank
    def __ne__(self, other):
        return not self == other
    def __lt__(self, other):
        return self.num_ranking < other.num_ranking
    def __le__(self, other):
        return self == other or self < other
    def __gt__(self, other):
        return not self <= other
    def __ge__(self, other):
        return self == other or self > other


class PokerHand(object):
    _num_cards = 5
    _hand_names = ['straight flush',
                   'four of a kind',
                   'full house',
                   'flush',
                   'straight',
                   'three of a kind',
                   'two pair',
                   'one pair',
                   'nothing']
    @classmethod
    def hand_rank(cls, name):
        return len(cls._hand_names) - cls._hand_names.index(name)
    @classmethod
    def multiplicities(cls, pcs):
        same_rank_as = lambda c: filter(lambda cc: c.rank == cc.rank, pcs)
        return [len(same_rank_as(pc)) for pc in pcs]
    @classmethod
    def num_unique_ranks(cls, pcs):
        return len(set(pc.rank for pc in pcs))
    def __init__(self, pcs):
        self.cards = pcs
        self.ranking = self.hand_rank(self.name)
    @property
    def cards(self):
        return self._cards
    @cards.setter
    def cards(self, cs):
        if len(cs) != self._num_cards:
            raise ValueError('Invalid poker hand: {} cards provided'.format(len(cs)))
        #elif any(str(cs[ii]) == str(c) for ii in range(len(cs)-1) for c in cs[ii+1:]):
        #    raise ValueError('Hand contains a duplicate card')
        else:
            self._cards = cs
    def mult(self, m, c):
        return self.multiplicities(self.cards)[self.cards.index(c)] == m
    def card_strs(self):
        return [str(c) for c in self.cards]
    def __str__(self):
        return ' '.join(self.card_strs())
    def __lt__(self, other):
        if self.ranking == other.ranking:
            srt = lambda c, o: (o.multiplicities(o.cards)[o.cards.index(c)], c)
            ss = list(sorted(self.cards, key=lambda c: srt(c, self), reverse=True))
            so = list(sorted(other.cards, key=lambda c: srt(c, other), reverse=True))
            for ii in range(self._num_cards):
                if ss[ii] == so[ii]: continue
                else: return ss[ii] < so[ii]
        else:
            return self.ranking < other.ranking
    def __eq__(self, other):
        return not self < other and not other < self


class Flush(PokerHand):
    @classmethod
    def is_flush(cls, pcs):
        return len(set(c.suit for c in pcs)) == 1
    @property
    def name(self):
        return 'flush'


class Straight(PokerHand):
    @classmethod
    def is_straight(cls, pcs):
        card_rank = lambda ii: sorted(pcs)[ii].num_ranking
        card_nums = range(cls._num_cards-1)
        return all(card_rank(ii+1) == card_rank(ii)+1 for ii in card_nums)
    @property
    def name(self):
        return 'straight'


class StraightFlush(PokerHand):
    @classmethod
    def is_straight_flush(cls, pcs):
        return Straight.is_straight(pcs) and Flush.is_flush(pcs)
    @property
    def name(self):
        return 'straight flush'


class FourOfAKind(PokerHand):
    @classmethod
    def is_four_of_a_kind(cls, pcs):
        return set(cls.multiplicities(pcs)) == set([1, 4])
    @property
    def name(self):
        return 'four of a kind'


class FullHouse(PokerHand):
    @classmethod
    def is_full_house(cls, pcs):
        return set(cls.multiplicities(pcs)) == set([2, 3])
    @property
    def name(self):
        return 'full house'


class ThreeOfAKind(PokerHand):
    @classmethod
    def is_three_of_a_kind(cls, pcs):
        return set(cls.multiplicities(pcs)) == set([1, 3])
    @property
    def name(self):
        return 'three of a kind'


class TwoPair(PokerHand):
    @classmethod
    def is_two_pair(cls, pcs):
        return set(cls.multiplicities(pcs)) == set([1, 2]) and cls.num_unique_ranks(pcs) == 3
    @property
    def name(self):
        return 'two pair'


class OnePair(PokerHand):
    @classmethod
    def is_one_pair(cls, pcs):
        return set(cls.multiplicities(pcs)) == set([1, 2]) and cls.num_unique_ranks(pcs) == 4
    @property
    def name(self):
        return 'one pair'


class Nothing(PokerHand):
    @classmethod
    def is_nothing(cls, pcs):
        is_not_straight = not Straight.is_straight(pcs)
        is_not_flush = not Flush.is_flush(pcs)
        has_no_duplicates = cls.num_unique_ranks(pcs) == cls._num_cards
        return is_not_straight and is_not_flush and has_no_duplicates
    @property
    def name(self):
        return 'nothing'


class PokerHandFactory(object):
    def __new__(cls, card_string_list):
        dispatcher = [(StraightFlush.is_straight_flush, StraightFlush),
                      (FourOfAKind.is_four_of_a_kind,   FourOfAKind),
                      (FullHouse.is_full_house,         FullHouse),
                      (Flush.is_flush,                  Flush),
                      (Straight.is_straight,            Straight),
                      (ThreeOfAKind.is_three_of_a_kind, ThreeOfAKind),
                      (TwoPair.is_two_pair,             TwoPair),
                      (OnePair.is_one_pair,             OnePair),
                      (Nothing.is_nothing,              Nothing)]
        pcs = [PlayingCard(c) for c in card_string_list]
        for (test, hand) in dispatcher:
            if test(pcs): return hand(pcs)
        raise ValueError('Not a poker hand: {}'.format(' '.join(card_string_list)))


def poker(hands):
    poker_hands = [PokerHandFactory(hand) for hand in hands]
    top_hand = max(poker_hands)
    top_hands = filter(lambda h: h == top_hand, poker_hands)
    return map(PokerHand.card_strs, top_hands)
