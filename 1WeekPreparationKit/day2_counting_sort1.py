#!/bin/python3

import math
import os
import random
import re
import sys

def countingSort(arr):
    # Her bir öğenin tekrar sayısını saklamak için bir liste oluşturuyoruz.
    counts = [0] * 100  # Problemin belirtildiği gibi, öğeler 0 ile 99 arasında olabilir.

    # Diziyi tarayarak her bir öğenin tekrar sayısını hesaplıyoruz.
    for num in arr:
        counts[num] += 1

    # Her bir öğenin tekrar sayısını içeren diziyi döndürüyoruz.
    return counts

# Ana programın başlangıcı
if __name__ == '__main__':
    # Çıktıyı bir dosyaya yazmak için dosyayı açıyoruz
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Kullanıcıdan dizinin boyutunu alıyoruz
    n = int(input().strip())

    # Kullanıcıdan diziyi alıyoruz ve integer'a dönüştürüyoruz
    arr = list(map(int, input().rstrip().split()))

    # countingSort fonksiyonunu çağırarak sonucu buluyoruz
    result = countingSort(arr)

    # Sonucu dosyaya yazıyoruz
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    # Dosyayı kapatıyoruz
    fptr.close()
