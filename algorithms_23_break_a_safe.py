from itertools import permutations

nums = [1,5,8]
tmp = list(permutations(nums*2, 4))
attempts = []

for i in tmp:
    qual = 1
    for k in nums:        
        if k not in i:
            qual *= 0
    if qual == 1:
        attempts.append(i)
        
attempts = list(dict.fromkeys(attempts))
        
for i in attempts:
    print(" ".join(map(str, i)))