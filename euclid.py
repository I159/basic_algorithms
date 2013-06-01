#!/usr/env/python python

def euclid(a, b):
    if not a or not b:
        raise ZeroDivisionError
    c = a % b
    if c:
        return euclid(b, c)
    return b


s_eucl = lambda a, b: b == 0 and a or s_eucl(b, a % b)


def test():
    leucl = euclid(27, 243)
    seucl = s_eucl(27, 243)
    print leucl, seucl
    assert leucl == seucl
