euclid = lambda m, n: m if n==0 else euclid(n, m%n)


def fib(a, lim):
    b = a
    while b < lim:
        yield b
        a, b = b, a+b


