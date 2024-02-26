import numpy as np

# Matris boyutlarını al
N ,M = map(int, input().split())

# Matrisi al
matrix = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrix.append(row)

# Numpy dizesine dönüştür
matrix = np.array(matrix)

# Transpozunu al
transpose_matrix = np.transpose(matrix)

# Flatten halini al
flatten_matrix = matrix.flatten()

# Sonuçları yazdır
print(transpose_matrix)
print(flatten_matrix)