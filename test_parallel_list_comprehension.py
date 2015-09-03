#!/usr/bin/env python3

import multiprocessing
import sympy as sym
import time

try:
    cpus = multiprocessing.cpu_count()
except NotImplementedError:
    cpus = 2

pool = multiprocessing.Pool(processes=cpus)
t = time.time()
num_primes = pool.map(sym.isprime, range(1, int(1e6)))
elapsed = time.time() - t

print("Com multiprocessamento: ", elapsed)

t = time.time()
num_primes = len([sym.isprime(x) for x in range(1, int(1e6))])
elapsed = time.time() - t
print("Sem multiprocessamento: ", elapsed)


