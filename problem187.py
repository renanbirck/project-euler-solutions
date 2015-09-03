#!/usr/bin/env python3

import sympy as sym
import multiprocessing

def is_semiprime(n):
    factors = sym.factorint(n)
    if len(factors) == 2:
        return n
    if len(factors.values()) == 1 and list(factors.values())[0] == 2:
        return n
    return 0


pool = multiprocessing.Pool(processes=8)
# Build a list of all semiprimes
semiprimes = pool.map(is_semiprime, range(1, int(1e8)))

print(sum(semiprimes))
