from itertools import product

# Girişleri al
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Kartezyen çarpımını hesapla
cartesian_product = list(product(A, B))

# Çıktıyı formatla ve yazdır
for item in cartesian_product:
    print(item, end=' ')