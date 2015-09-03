#!/usr/bin/python3

import functools

@functools.lru_cache(maxsize=None)
def are_amicable(x,y):
    if x==y or x == 0 or y == 0: return False
    sum_x=sum(e for e in range(1, x//2+1) if x%e==0)
    sum_y=sum(e for e in range(1, y//2+1) if y%e==0)
    return sum_x==y and sum_y==x
acc = 0
for a in range(1, 10000):
    for b in range(1, a):
        if are_amicable(a, b):
            acc = acc + a + b
            print(a, b)

print(acc)
print(are_amicable.cache_info())
