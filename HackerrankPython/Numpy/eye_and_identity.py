import numpy as np

# Girdiyi al ve boyutları al
N, M = map(int, input().split())

# Birim matrisi oluştur
array = np.eye(N, M)

# Uyumluluk sorununu ortadan kaldır ve sonucu yazdır
np.set_printoptions(legacy="1.13")
print(array)
