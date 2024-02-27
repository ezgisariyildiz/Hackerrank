from itertools import product

K, M = map(int, input().split())

lists = []
for _ in range(K):
    lists.append(list(map(int, input().split()[1:])))

max_val = 0
for combination in product(*lists):
    s = sum(x ** 2 for x in combination) % M
    if s > max_val:
        max_val = s

print(max_val)