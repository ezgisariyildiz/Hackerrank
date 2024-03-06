import numpy as np

# Boyutları al
N, M = map(int, input().split())

# Dizileri al
A = np.array([input().split() for _ in range(N)], int)
B = np.array([input().split() for _ in range(N)], int)

# İşlemleri gerçekleştir ve sonuçları yazdır
print(A + B)
print(A - B)
print(A * B)
print(A // B)
print(A % B)
print(A ** B)
