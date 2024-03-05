# ***************DAY2: MOCK TEST: FLIPPING THE MATRIX********************

import math
import os
import random
import re
import sys

# flipping the matrix fonksiyonu. verilen matrisi dört eşit parçaya böler ve
# her bir parçanın maksimum değerlerini toplayarak sonucu döndürür

def flippingMatrix(matrix):
    # Matrisin boyutunun yarısı matrisi dört eşit parçaya bölmek için kullanılacak
    n = len(matrix) // 2

    max_sum = 0
    for i in range(n):
        for j in range(n):
            # Her bir parçanın maksimum değerini bulup toplama ekleyelim
            max_sum += max(matrix[i][j], matrix[i][2 * n - j - 1], 
                           matrix[2 * n - i - 1][j], 
                           matrix[2 * n - i - 1][2 * n - j - 1])
        return max_sum
    
    if __name__ == '__main__':
         # Çıktıyı bir dosyaya yazmak için dosyayı açıyoruz
        fptr = open(os.environ['OUTPUT_PATH'], 'w')

        # Kullanıcıdan sorgu sayısını alıyoruz
        q = int(input().strip())

        # Her bir sorgu için
        for q_itr in range(q):
            # Matris boyutunu alıyoruz
            n = int(input().strip())

            # Matrisi oluşturmak için kullanıcıdan satırları alıyoruz
            matrix = []
            for _ in range(2 * n):
                matrix.append(list(map(int, input().rstrip().split())))

            # flippingMatrix fonksiyonunu çağırarak sonucu buluyoruz
            result = flippingMatrix(matrix)

            # Sonucu dosyaya yazıyoruz
            fptr.write(str(result) + '\n')

        # Dosyayı kapatıyoruz
        fptr.close()