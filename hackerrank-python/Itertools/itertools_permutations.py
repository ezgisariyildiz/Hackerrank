from itertools import permutations

# Girişleri al
S, k = input().split()
k = int(k)

# Permütasyonları hesapla ve leksikografik sırala
permutation_list = sorted(permutations(S, k))

# Sonucu yazdır
for perm in permutation_list:
    print(' '.join(perm))
    