#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    # Yeni bir boş liste oluşturduk
    new_grid = []

    # Her bir satır için
    for x in grid:
        # Karekterleri alfabetik sıralayıp new_grid e ekler
        new_grid.append("".join(sorted(x)))
        print(new_grid) # Aradaki adımı görmek için geçici yazdırdık

    # Yeni sıralı grid, orjinal grid ile değiştirilir
    grid = new_grid

    # Sıralı sütunları kontrol etmek için iki iç içe döngü oluşturulur
    # Dış döngü, sütun indexsini temsil eder, iç döngü satır indeksini
    for i in range(grid[0]):
        for j in range(len(grid)-1):
            # Sıralı sütunları kontrol ederken ASCII değerleri karşılaştırılır
            # Eğer bir alttaki satırdaki karakter bir üst satırdaki karakterden büyükse, sıralama bozulmuştur ve NO döndürülür
            if ord(grid[j][i]) > ord[grid[j+1][i]]:
                return "NO"
    
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Test sayısını alır.
    t = int(input().strip())

    # Her bir test durumu için:
    for t_itr in range(t):
        # Grid boyutunu alır.
        n = int(input().strip())

        grid = []

        # Grid'i oluşturur.
        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        # Sonucu hesaplar.
        result = gridChallenge(grid)

        # Sonucu çıktı dosyasına yazar.
        fptr.write(result + '\n')

    fptr.close()