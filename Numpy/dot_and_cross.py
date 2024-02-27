import numpy as np

# Boyutları al
N = int(input().split())

# İki diziyi al
A = np.array([input().split() for _ in range(N)], int)
B = np.array([input().split() for _ in range(N)], int)

# Matris çarpımı bul
result = np.dot(A, B)

# Sonucu yazdır
print(result)