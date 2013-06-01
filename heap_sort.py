#!/usr/bin/env python
class HeapSort(object):
    def __init__(self, sqc):
        self.sqc = sqc
        self.size = len(sqc)
        self.heapify()

    def swap(self, i, j):
        print 'swap'
        self.sqc[i], self.sqc[j] = self.sqc[j], self.sqc[i]

    def siftdown(self, start, end=None):
        root = start
        while root * 2+1 <= end:
            child = (root * 2) + 1
            swap = root

            if self.sqc[swap] < self.sqc[child]:
                swap = child
            if child+1 <= end and self.sqc[swap] < self.sqc[child+1]:
                swap = child+1
            if swap != root:
                root = swap
            else:
                return


    def heapify(self):
        print 'heapify'
        p = (self.size/2)
        while p >= 0:
            print 'while size'
            p -= 1
            self.siftdown(p)
        return

    def sort(self, end=None):
        print 'sort'
        end = self.size if end is None else end
        if end <= 0:
            return self.sqc
        end -= 1
        self.swap(0, end)
        self.siftdown(0, end)
        self.sort(end)

def test_heap():
    h = [9,1,4,3,-123]
    HeapSort(h).sort()
    print 'h', h
