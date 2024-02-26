import numpy as np

# Boyutları al
N, M = map(int, input().split())

# Diziyi al
arr =np.array([input().split() for _ in range(N)], int)

# Ortalama, varyans ve standart sapmayı nul
mean_arr = np.mean(arr, axis=1)
var_arr = np.var(arr, axis=0)
std_arr = round(np.std(arr, axis=None), 11)

# Sonuçları yazdır
print(mean_arr)
print(var_arr)
print(std_arr)