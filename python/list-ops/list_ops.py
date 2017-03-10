# Please, do not use the built-in python functions like map, reduce, len, etc.
# that solve the same problems and try to solve it yourself instead.


def map_clone(function, xs):
    return [function(x) for x in xs]


def length(xs):
    l = 0
    for x in xs: l += 1
    return l


def filter_clone(function, xs):
    return [x for x in xs if function(x)]


def reverse(xs):
    return xs[::-1] if xs else []


def append(xs, y):
    return xs + [y]


def foldl(function, xs, acc):
    for x in xs: acc = function(acc, x)
    return acc


def foldr(function, xs, acc):
    for x in reverse(xs): acc = function(x, acc)
    return acc


def flat(xs):
    fxs = []
    for x in xs:
        if not isinstance(x, list): fxs += [x]
        else: fxs += [xx for xx in flat(x)]
    return fxs


def concat(xs, ys):
    xsys = []
    if xs is not None:
        for x in xs: xsys += [x]
    if ys is not None:
        for y in ys: xsys += [y]
    return xsys
