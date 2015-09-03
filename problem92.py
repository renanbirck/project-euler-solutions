#!/usr/bin/env python3

import functools

def numberchain(n):
    n_list = list(str(n))
    n_list = sum([int(n)**2 for n in n_list])
    return n_list

def repeated_number_chain(n):
    next_n = n
    while not (next_n == 1 or next_n == 89):
        next_n = numberchain(next_n)
    return next_n

acc = 0
for i in range(1, 1000000):
    if(i % 10000 == 0):
        print(i, " acc = ", acc)
    k = repeated_number_chain(i)
    if k == 89:
        acc = acc + 1

print(acc)
