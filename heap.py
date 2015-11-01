#!/usr/bin/env python
#-*-coding: utf-8-*-
import cProfile
from random import randrange

from tracer_bullet import trace
# Examples

def heap_sort1(sqc):
    def down_heap(sqc, k, n):
        parent = sqc[k]

        while 2*k+1 < n:
            child = 2*k+1
            if child+1 < n and sqc[child] < sqc[child+1]:
                child += 1
            if parent >= sqc[child]:
                break
            sqc[k] = sqc[child]
            k = child
        sqc[k] = parent

    size = len(sqc)

    for i in range(size/2-1, -1, -1):
        down_heap(sqc, i, size)

    for i in range(size-1, 0, -1):
        sqc[0], sqc[i] = sqc[i], sqc[0]
        down_heap(sqc, 0, i)


def heap_sort2(sqc):
    def swap(i, j):
        sqc[i], sqc[j] = sqc[j], sqc[i]

    def heapify(end,i):
        l=2 * i + 1
        r=2 * (i + 1)
        max=i
        if l < end and sqc[i] < sqc[l]:
           max = l
        if r < end and sqc[max] < sqc[r]:
           max = r
        if max != i:
            swap(i, max)
            heapify(end, max)

    end = len(sqc)
    start = end / 2 - 1
    for i in range(start, -1, -1):
        heapify(end, i)
    for i in range(end-1, 0, -1):
        swap(i, 0)
        heapify(i, 0)


# My own implementation
def heapsortV1_0(sequence):
    sequence_length = len(sequence)

    def swap_if_greater(parent_index, child_index):
        if sequence[parent_index] < sequence[child_index]:
            sequence[parent_index], sequence[child_index] =\
                    sequence[child_index], sequence[parent_index]

    def sift(parent_index, unsorted_length):
        index_of_greater = lambda a, b: a if sequence[a] > sequence[b] else b
        while parent_index*2+2 < unsorted_length:
            left_child_index = parent_index*2+1
            right_child_index = parent_index*2+2

            greater_child_index = index_of_greater(left_child_index,
                    right_child_index)

            swap_if_greater(parent_index, greater_child_index)

            parent_index = greater_child_index

    def heapify():
        for i in range((sequence_length/2)-1, -1, -1):
            sift(i, sequence_length)

    def sort():
        count = sequence_length
        while count > 0:
            count -= 1
            swap_if_greater(count, 0)
            sift(0, count)

    heapify()
    sort()

# n = len(s)
@trace
def heapsortV1_1(s): # 1
    """The most effective implementation.
    A last parent element deprived the right child element does not need to
    heapifying, because at the end of the heapifying process, location of the
    last element will take the greatest sorted element."""

    sl = len(s) # 1 * n

    def swap(pi, ci): # (n-2) + ((n/2) * log(n/2)) + ((n-2) * log(n-2))
        if s[pi] < s[ci]: # (n-2) + ((n/2) * log(n/2)) + ((n-2) * log(n-2))
            s[pi], s[ci] = s[ci], s[pi] # ?

    def sift(pi, unsorted): # (n/2) + (n-2)
        i_gt = lambda a, b: a if s[a] > s[b] else b # ((n/2) * log(n/2)) + ((n-2) * log(n-2))
        while pi*2+2 < unsorted: # (n/2) + (n-2)
            gtci = i_gt(pi*2+1, pi*2+2) # ((n/2) * log(n/2)) + ((n-2) * log(n-2))
            swap(pi, gtci) # ((n/2) * log(n/2)) + ((n-2) * log(n-2))
            pi = gtci # ((n/2) * log(n/2)) + ((n-2) * log(n-2))
    # heapify
    for i in range((sl/2)-1, -1, -1): # n/2
        sift(i, sl) # n/2
    # sort
    for i in range(sl-1, 0, -1): # n-2
        swap(i, 0) # n-2
        sift(0, i) # n-2


def heapsortV2(s):
    sl = len(s)

    def swap(pi, ci):
        s[pi], s[ci] = s[ci], s[pi]

    def sift(pi, unsorted):
        i_gt = lambda a, b: a if s[a] > s[b] else b
        while pi*2+1 < unsorted:
            lchi, rchi = pi*2+1, pi*2+2
            gtci = i_gt(lchi, rchi) if rchi < unsorted else lchi
            swap(pi, gtci)
            pi = gtci
    # heapify
    for i in range((sl/2)-1, -1, -1):
        sift(i, sl)
    # sort
    for i in range(sl-1, 0, -1):
        swap(i, 0)
        sift(0, i)

def heapsortV3(s):
    sl = len(s)

    def swap(pi, ci):
        if s[pi] < s[ci]:
            s[pi], s[ci] = s[ci], s[pi]

    def sift(pi, unsorted):
        i_gt = lambda a, b: a if s[a] > s[b] else b
        while pi*2+1 < unsorted:
            lchi, rchi = pi*2+1, pi*2+2
            gtci = i_gt(lchi, rchi) if rchi < unsorted else lchi
            swap(pi, gtci)
            pi = gtci
    # heapify
    for i in range((sl/2)-1, -1, -1):
        sift(i, sl)
    # sort
    for i in range(sl-1, 0, -1):
        swap(i, 0)
        sift(0, i)


class TestHeapSort(object):
    def heapsort(self, sqc):
        return heapsortV1_1(sqc)

    def test_arrays_of_different_lengths(self):
        arrays = ([randrange(-100, 100) for v in [1]* i] for i in range(100))
        for i in arrays:
            self.heapsort(i)

        for i in arrays:
            count = 0
            while count <= len(i)-2:
                assert i[count] <= i[count+1]
                count += 1

    def test_1_unsorted_array(self):
        array = [randrange(-100, 100) for i in [1]*100]
        self.heapsort(array)
        count = 0
        while count <= len(array)-2:
            array[count] <= array[count+1]
            count += 1


    def test_empty_array(self):
        assert self.heapsort([]) == None

    def test_sorted_array(self):
        n = range(100)
        self.heapsort(n)
        count = 0
        while count <= len(n)-2:
            assert n[count] <= n[count+1]
            count += 1


class TestHeapSort3(TestHeapSort):
    def heapsort(self, sqc):
        return heapsortV2(sqc)


class TestHeapSort4(TestHeapSort):
    def heapsort(self, sqc):
        return heapsortV3(sqc)


class TestRuntime(object):
    a = b = c = [randrange(-100, 100) for i in [1]*100]
    def test_runtime1(self):
        print '''
=============================================================
        heapsortV1_1:
============================================================='''
        print cProfile.runctx('heapsortV1_1(self.a)', globals(), locals())

    def test_runtime2(self):
        print '''
=============================================================
        heapsortV2:
============================================================='''
        print cProfile.runctx('heapsortV2(self.b)', globals(), locals())

    def test_runtime3(self):
        print '''
=============================================================
        heapsortV3:
============================================================='''
        print cProfile.runctx('heapsortV3(self.c)', globals(), locals())


if __name__ == '__main__':
    heapsortV1_1([randrange(-100, 100) for i in [1]*100])
