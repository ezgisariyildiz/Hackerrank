import numpy as np

np.set_printoptions(legacy="1.13")

# Matris boyutunu al
N = int(input())

# Matrisi oluştur
matrix = []
for _ in range(N):
    row = list(map(float, input().split()))
    matrix.append(row)

# Matrisin determinantını hesapla
determinant = np.linalg.det(matrix)

# Sonucu yazdır
print(determinant)