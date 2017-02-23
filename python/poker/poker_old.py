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
    _hands = ['straight flush',
              'four of a kind',
              'full house',
              'flush',
              'straight',
              'three of a kind',
              'two pair',
              'one pair',
              'nothing']
    def __init__(self, cards):
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
            self._cards = sorted(PlayingCard(c) for c in cs)
    @property
    def is_straight(self):
        this_rank = lambda ii: PlayingCard._ranks.index(self.cards[ii].rank)
        next_rank = lambda ii: this_rank(ii+1)
        indices = range(PokerHand._num_cards-1)
        return all(next_rank(ii) == this_rank(ii)+1 for ii in indices)
    @property
    def is_flush(self):
        return len(set(c.suit for c in self._cards)) == 1
    @property
    def is_straight_flush(self):
        return self.is_straight and self.is_flush
    def same_rank_as(self, c):
        return filter(lambda cc: c.rank == cc.rank, self._cards)
    @property
    def is_four_of_a_kind(self):
        return max(len(self.same_rank_as(c)) for c in self._cards) == 4
    @property
    def is_full_house(self):
        return set(len(self.same_rank_as(c)) for c in self._cards) == set([2, 3])
    @property
    def is_three_of_a_kind(self):
        return set(len(self.same_rank_as(c)) for c in self._cards) == set([1, 3])
    @property
    def is_two_pair(self):
        return [len(self.same_rank_as(c)) for c in self._cards] == [2, 2, 2, 2, 1]
    @property
    def is_one_pair(self):
        return [len(self.same_rank_as(c)) for c in self._cards] == [2, 2, 1, 1, 1]
    @property
    def is_nothing(self):
        return not self.is_straight and [len(self.same_rank_as(c)) for c in self._cards] == [1]*5
    @property
    def hand_rank(self):
        rank_tests = [self.is_straight_flush,
                      self.is_four_of_a_kind,
                      self.is_full_house,
                      self.is_flush,
                      self.is_straight,
                      self.is_three_of_a_kind,
                      self.is_two_pair,
                      self.is_one_pair,
                      self.is_nothing]
        for t in rank_tests:
            if t:
                return len(rank_tests)-1 - rank_tests.index(t)
    def print_thing(self):
        print([len(self.same_rank_as(c)) for c in self._cards])
    def to_str(self):
        return map(str, self.cards)
    def __str__(self):
        return ' '.join(self.to_str())
    def __lt__(self, other):
        if self.hand_rank == other.hand_rank:
            return max(c.rank for c in self.cards) < max(c.rank for c in other.cards)
        else:
            return self.hand_rank < other.hand_rank


def poker(hs):
    hands = [PokerHand(h) for h in hs]
    return [h.to_str() for h in hands]


if __name__=='__main__':
    def print_true(T):  print('True:  {}'.format(T))
    def print_false(F): print('False: {}'.format(F))
    fourOfAKind = PokerHand('4H 4S 4C 4D 9H'.split())
    straightTo8 = PokerHand('4S 6H 7S 8D 5H'.split())
    full = PokerHand('4S 5H 4D 5D 4H'.split())
    threeOf4 = PokerHand('4S 5H 4D 8D 4H'.split())
    pairOf2 = PokerHand('4S 2H 6S 2D JH'.split())
    doublePair = PokerHand('4S 5H 4C 8D 5D'.split())
    straightFlushTo9 = PokerHand('5S 7S 8S 9S 6S'.split())
    print(straightFlushTo9.hand_rank)
