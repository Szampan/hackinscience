from itertools import permutations

cleans = ['1', '5', '8']

for o in cleans:
    for p in permutations(cleans + [o], 4):
        print(' '.join(p))