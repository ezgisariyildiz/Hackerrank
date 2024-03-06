import numpy as np

# Girdiyi al
input_str = input()

# Boşluklarla ayrılmış olarak 9 tane sayıyı bir liste olarak al
input_list = list(map(int, input_str.split()))

# Listeyi 3x3 Numpy dizesine dönüştür
array = np.array(input_list).reshape(3, 3)

# Numpy dizisini yazdır
print(array)