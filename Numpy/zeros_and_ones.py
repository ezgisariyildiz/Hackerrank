import numpy as np

# Girdiyi al ve boyutları al
shape = tuple(map(int, input().split()))

# Sıfırlar dizesini oluştur
zeros_array = np.zeros(shape, dtype=int)

# Birler dizesini oluştur
ones_array = np.ones(shape, dtype=int)

# Sonuçları yazdır
print(zeros_array)
print(ones_array)