to_ocr = {'0' : [" _ ",
                 "| |",
                 "|_|",
                 "   "],
          '1' : ["   ",
                 "  |",
                 "  |",
                 "   "],
          '2' : [" _ ",
                 " _|",
                 "|_ ",
                 "   "],
          '3' : [" _ ",
                 " _|",
                 " _|",
                 "   "],
          '4' : ["   ",
                 "|_|",
                 "  |",
                 "   "],
          '5' : [" _ ",
                 "|_ ",
                 " _|",
                 "   "],
          '6' : [" _ ",
                 "|_ ",
                 "|_|",
                 "   "],
          '7' : [" _ ",
                 "  |",
                 "  |",
                 "   "],
          '8' : [" _ ",
                 "|_|",
                 "|_|",
                 "   "],
          '9' : [" _ ",
                 "|_|",
                 " _|",
                 "   "]}

from_ocr = {''.join(v) : k for k, v in to_ocr.iteritems()}

def single_number(grid):
    if not (len(grid) == 4 and all(len(string) == 3 for string in grid)):
        raise ValueError('Invalid grid')
    grid_string = ''.join(grid)
    return from_ocr[grid_string] if grid_string in from_ocr.keys() else '?'

def number(grid):
    num_dgts = len(grid) / 3
    dgt_grids = [[s[ii:ii+3] for s in grid] for ii in xrange(0,len(grid[0]),3)]
    return ''.join(single_number(g) for g in dgt_grids)

def grid(number):
    try:
        dgt_grids = [to_ocr[d] for d in number]
        return [''.join(g[ii] for g in dgt_grids) for ii in range(4)]
    except KeyError:
        raise ValueError('Invalid number: {}'.format(number))
