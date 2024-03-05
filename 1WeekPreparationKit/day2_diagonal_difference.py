import math
import os
import random
import re
import sys

# DiagonalDifference fonksiyonu, bir matrisin ana ve yan diagonalındaki elemanların farkını hesaplar
def diagonalDifference(arr):
    # MAtrisin boyutunu alalım
    n = len(arr)

    # İlk olarak ana diagonaldaki elemanların toplamını hesaplayalım
    primary_diagonal_sum = 0
    for i in range(n):
        primary_diagonal_sum += arr[i][i]

        # Ardından yan diagonaldaki elemanların toplamını hesaplayalım
        secondary_diagonal_sum = 0
        for i in range(n):
            secondary_diagonal_sum += arr[i][n - i - 1]

        # Farkı hesaplayalım ve mutlak değerini alalım
        difference = abs(primary_diagonal_sum - secondary_diagonal_sum)

        return difference
    
if __name__ == '__main__':
    # Çıktıyı bir dosyaya yazmak için dosyayı açıyoruz
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Kullanıcıdan matrisin boyutunu al
    n = int(input().strip())

    # Matrisi oluşturmak için kullanıcıdan satırları alıyoruz
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    # diagonalDifference fonksiyonunu çağırarak sonucu bul
    result = diagonalDifference(arr)

    # Sonucu dosyaya yaz
    fptr.write(str(result) + '\n')

    # Dosyayı kapat
    fptr.close()