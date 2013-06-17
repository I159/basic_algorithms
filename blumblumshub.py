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
