#!/usr/bin/python3
# coding: utf-8

NAMES_FILE = 'p022_names.txt'

def name_score(name):
    name_list = list(name)
    name_scores = [ord(x)-64 for x in name_list]
    return sum(name_scores)

with open(NAMES_FILE, 'r') as f:
    names = f.readlines()

names = names[0].replace('"','').split(",")
names.sort()

scores = 0

for (position, name) in enumerate(names):
    # "position" starts from 0 rather than 1, let's compensate that.
    scores = scores + ((position+1) * name_score(name))

print(scores)
