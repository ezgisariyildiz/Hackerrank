import numpy as np

# Katsayıları al
coefficients = np.array(input().split(), float)

# Noktayı al
x = float(input())

# Polinomun değerini hesapla
result = np.polyval(coefficients, x)

# Sonucu yazdır
print(result)