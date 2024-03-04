import numpy as np

# Dizileri al
A = np.array(input().split(), int)
B = np.array(input().split(), int)

# İç çarpımı hesapla
inner_product = np.inner(A, B)

# Dış çarpımı hesapla
outer_product = np.outer(A, B)

# Sonuçları yazdır
print(inner_product)
print(outer_product)