import numpy as np

np.set_printoptions(legacy="1.13")
# Girdiyi al ve diziyi oluştur
A = np.array(int(input().split(), float))

# Floor, ceil ve rint değerlerini bul

floor_A = np.floor(A)
ceil_A = np.ceil(A)
rint_A = np.rint(A)

# Sonuçları yazdır
print(floor_A)
print(ceil_A)
print(rint_A)