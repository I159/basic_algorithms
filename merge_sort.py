import collections
from random import randrange


def split(arr):
    if not isinstance(arr[0], collections.Iterable):
        arr = [[i, ] for i in arr]
    odd = arr.pop(-1) if len(arr) % 2 else None
    coupled = zip(*[iter(arr)]*2)
    coupled = [list(i) for i in coupled]
    if odd:
        coupled.append([odd, []])
    return coupled


def merge(arr1, arr2):
    i = j = 0
    new_l = []
    while True:
        try:
            if arr1[i] <= arr2[j]:
                new_l.append(arr1[i])
                i += 1
            else:
                new_l.append(arr2[j])
                j += 1
        except IndexError:
            break
    residue = arr1[i:] or arr2[j:]
    new_l += residue
    return new_l


def sort(arr):
    coupled = split(arr)
    i = 0
    while i < len(coupled):
        coupled[i] = merge(*coupled[i])
        i += 1
    if len(coupled) > 1:
        return sort(coupled)
    return coupled[0]


def test():
    arr = [randrange(100) for i in range(100)]
    if not sorted(arr) == sort(arr):
        print sort(arr)
    else:
        print 'SORTED'


if __name__ == "__main__":
    test()
