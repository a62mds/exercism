#!/usr/bin/env python

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
        if r in PlayingCard._ranks:
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
    def __str__(self):
        return ''.join([self.rank, self.suit])
    def __eq__(self, other):
        return self.rank == other.rank
    def __ne__(self, other):
        return not self == other
    def __lt__(self, other):
        return PlayingCard._ranks.index(self.rank) < PlayingCard._ranks.index(other.rank)
    def __le__(self, other):
        return self == other or self < other
    def __gt__(self, other):
        return not self <= other
    def __ge__(self, other):
        return self == other or self > other


class PokerHand(object):
    _num_cards = 5
    def __init__(self, cards):
        print('in PokerHand.__init__')
        self.cards = cards
    @property
    def cards(self):
        return self._cards
    @cards.setter
    def cards(self, cs):
        if len(cs) != PokerHand._num_cards:
            raise ValueError('Invalid poker hand: {} cards provided'.format(len(cs)))
        elif any(cs[ii] == c for ii in range(len(cs)-1) for c in cs[ii+1:]):
            raise ValueError('Hand contains a duplicate card')
        else:
            self._cards = cs
    def to_str(self):
        return [str(c) for c in self.cards]
    def __str__(self, cards):
        return ' '.join(self.to_str())
    def __lt__(self, other):
        if self.hand_rank == other.hand_rank:
            # YOU ARE HERE
            return False
        else:
            return self.hand_rank < other.hand_rank

class StraightFlush(PokerHand):
    def __new__(cls, cards):
        instance = object.__new__(StraightFlush, cards)
        return instance
    def __init__(self, cards):
        super


class FourOfAKind(object):
    pass


class FullHouse(object):
    pass


class Flush(object):
    pass


class Straight(object):
    pass


class ThreeOfAKind(object):
    pass


class TwoPair(object):
    pass


class OnePair(object):
    pass


class Nothing(object):
    pass


class PokerHandFactory(type):
    #### think about a factory method here which instantiates a different class
    #### of PokerHands, with the hand determined by your tests
    def __new__(cls, cards):
        print('in PokerHand.__new__')
        _hands = {cls.is_straight_flush  : StraightFlush,
                  cls.is_four_of_a_kind  : FourOfAKind,
                  cls.is_full_house      : FullHouse,
                  cls.is_flush           : Flush,
                  cls.is_straight        : Straight,
                  cls.is_three_of_a_kind : ThreeOfAKind,
                  cls.is_two_pair        : TwoPair,
                  cls.is_one_pair        : OnePair,
                  cls.is_nothing         : Nothing}
        _cards = sorted(PlayingCard(c) for c in cards)
        for test, Hand in _hands.iteritems():
            if test(_cards):
                return super(PokerHandFactory, Hand).__new__(Hand, _cards)
        raise Exception('Invalid poker hand')
    @classmethod
    def is_straight(cls, cards):
        this_rank = lambda ii: PlayingCard._ranks.index(cards[ii].rank)
        next_rank = lambda ii: this_rank(ii+1)
        indices = range(PokerHand._num_cards-1)
        return all(next_rank(ii) == this_rank(ii)+1 for ii in indices)
    @classmethod
    def is_flush(cls, cards):
        return len(set(c.suit for c in cards)) == 1
    @classmethod
    def is_straight_flush(cls, cards):
        return cls.is_straight(cards) and cls.is_flush(cards)
    @classmethod
    def same_rank_as(cls, c, cards):
        return filter(lambda cc: c.rank == cc.rank, cards)
    @classmethod
    def is_four_of_a_kind(cls, cards):
        return max(len(cls.same_rank_as(c, cards)) for c in cards) == 4
    @classmethod
    def is_full_house(cls, cards):
        return set(len(cls.same_rank_as(c, cards)) for c in cards) == set([2, 3])
    @classmethod
    def is_three_of_a_kind(cls, cards):
        return set(len(cls.same_rank_as(c, cards)) for c in cards) == set([1, 3])
    @classmethod
    def is_two_pair(cls, cards):
        return [len(cls.same_rank_as(c, cards)) for c in cards] == [2, 2, 2, 2, 1]
    @classmethod
    def is_one_pair(cls, cards):
        return [len(cls.same_rank_as(c, cards)) for c in cards] == [2, 2, 1, 1, 1]
    @classmethod
    def is_nothing(cls, cards):
        return not cls.is_straight(cards) and [len(cls.same_rank_as(c, cards)) for c in cards] == [1]*5




def poker(hs):
    hands = [PokerHand(h) for h in hs]
    return [h.to_str() for h in hands]


if __name__=='__main__':
    """
    def print_true(T):  print('True:  {}'.format(T))
    def print_false(F): print('False: {}'.format(F))
    fourOfAKind = PokerHand('4H 4S 4C 4D 9H'.split())
    straightTo8 = PokerHand('4S 6H 7S 8D 5H'.split())
    full = PokerHand('4S 5H 4D 5D 4H'.split())
    threeOf4 = PokerHand('4S 5H 4D 8D 4H'.split())
    pairOf2 = PokerHand('4S 2H 6S 2D JH'.split())
    doublePair = PokerHand('4S 5H 4C 8D 5D'.split())
    """
    straightFlushTo9 = PokerHandFactory('5S 7S 8S 9S 6S'.split())
    #print(straightFlushTo9.rank)
