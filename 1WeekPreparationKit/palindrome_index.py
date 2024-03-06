# ***************DAY3: MOCK TEST: PALINDROME INDEX********************

import math
import os
import random
import re
import sys

def palindromeIndex(s):
    # Verilen bir karakter dizisinin bir palindrom olması için gereken indeksi bulan fonksiyon
    n = len(s)  # Karakter dizisinin uzunluğunu hesapla
    for i in range(n // 2):  # Karakter dizisinin yarısına kadar bir döngü oluştur
        if s[i] != s[n - 1 - i]:  # Karakterlerin karşılıklı olup olmadığını kontrol et
            # Karakteri kaldırdığımızda palindrom oluşup oluşmayacağını kontrol etmek için alt dizeleri oluştur
            left_substring = s[i + 1 : n - i]  # Başlangıçtaki karakterden bir sonraki karakterden, sondaki karakterden bir önceki karaktere kadar olan alt dize
            right_substring = s[i + 1 : n - i][::-1]  # Bu alt dizeyi ters çevirerek elde edilen alt dize
            if left_substring == right_substring:  # İki alt dize aynı mı diye kontrol et
                return i  # Eğer aynıysa, i indeksini döndür (başlangıçtaki karakteri kaldırarak bir palindrom oluşturur)
            else:
                return n - 1 - i  # Aksi takdirde, n - 1 - i indeksini döndür (sondaki karakteri kaldırarak bir palindrom oluşturur)
    return -1  # Eğer karakter dizisi zaten bir palindromsa, -1 döndür

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
