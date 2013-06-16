#!/usr/bin/env python
import random

from erathosphenes import erathosphenes as e


class BlumBlumShub(object):
    def __init__(self, length):
        self.length = length
        self.primes = e(1000)

    def gen_primes(self):
        out_primes = []
        while len(out_primes) < 2:
            curr_prime = self.primes[random.randrange(len(self.primes))]
            if curr_prime % 4 == 3:
                out_primes.append(curr_prime)
        return out_primes

    def random_generator(self):
        x = random.randrange(1000000)
        while self.length:
            x += 1
            p, q = self.gen_primes()
            m = p * q
            z = (x**2) % m
            self.length -= 1
            yield str(bin(z).count('1') % 2)

    def get_random_bits(self):
        return ''.join(self.random_generator())


def test_blumblumshub():
    b = (BlumBlumShub(100) for i in range(9))
    for i in b:
        for v in b:
            assert v != i







#class BlumBlumShub(object):
#    def __init__(self, bits):
#        self.n = self.gen_n(bits)
#        length = self.bit_len(self.n)
#        seed = randrange(length)
#        self.set_seed(seed)
#
#    def get_prime(self, up_to):
#        primes = erathosphenes(up_to)
#        while primes:
#            p = primes.pop(choice(primes))
#            if p % 4 == 3:
#                return p
#
#    def gen_n(self, bits):
#        p = self.get_prime(bits/2)
#        q = self.get_prime(bits/2)
#        while p == q:
#            q = self.get_prime(bits/2)
#        return p * q
#
#    def set_seed(self, seed):
#        self.state = seed % self.n
#
#    def bit_len(self, x):
#        assert x > 0
#        q = 0
#        while x:
#            q = q+1
#            x = x >> 1
#        return q
#
#    def next(self, num_bits):
#        result = 0
#        for i in range(num_bits, 0, -1):
#            self.state = (self.state**2) % self.n
#            result = (result << 1) | (self.state & 1)
#
#
#def test_blumblumshub():
#    blblsh = BlumBlumShub(1000)
#    print blblsh
