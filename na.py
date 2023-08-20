from itertools import permutations
s = permutations(input())
for x in s: 
    print(''.join(x))