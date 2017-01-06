class BeerSong(object):

    def __init__(self):
        self.line1 = "{0} bottles of beer on the wall, {0} bottles of beer.\n"
        self.line2 = ("Take one down and pass it around, "
                      "{0} bottles of beer on the wall.\n")
        self.second_verse = ("2 bottles of beer on the wall, 2 bottles of beer.\n"
                             "Take one down and pass it around, "
                             "1 bottle of beer on the wall.\n")
        self.first_verse = ("1 bottle of beer on the wall, 1 bottle of beer.\n"
                            "Take it down and pass it around, "
                            "no more bottles of beer on the wall.\n")
        self.zeroth_verse = ("No more bottles of beer on the wall, "
                             "no more bottles of beer.\n"
                             "Go to the store and buy some more, "
                             "99 bottles of beer on the wall.\n")

    def verse(self, num):
        if num == 0:
            return self.zeroth_verse
        elif num == 1:
            return self.first_verse
        elif num == 2:
            return self.second_verse
        else:
            return self.line1.format(num) + self.line2.format(num - 1)

    def song(self, start, end=0):
        return "\n".join(self.verse(nn) for nn in range(start, end-1, -1)) + "\n"


####

def verse(num):
    return BeerSong().verse(num)

def song(start, end=0):
    return BeerSong().song(start, end)
