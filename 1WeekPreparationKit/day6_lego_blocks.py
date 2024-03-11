#!/bin/python3

import os
import sys

MOD = 10**9 + 7

def legoBlocks(n, m):
    MOD = (10**9 +7)

    # Adım 1: O(W)
    # Tek bir satır oluşturmak için kombinasyon sayısı
    # Sadece dört farklı boyut olduğu için,
    # başlangıç durumları:
    # genişlik 0 ise, kombinasyon 1'dir
    # genişlik 1 ise, kombinasyon 1'dir
    # genişlik 2 ise, kombinasyon 2'dir
    # genişlik 3 ise, kombinasyon 4'tür
    row_combinations = [1, 1, 2, 4]
    
    # Geçerli duvarın genişliğine kadar satır kombinasyonlarını oluştur
    while len(row_combinations) <= m: 
        row_combinations.append(sum(row_combinations[-4:]) % MOD)
    
    # Adım 2: O(W)
    # Değişen genişlikteki N yüksekliğindeki bir duvarın toplam kombinasyonlarını hesapla
    total = [pow(c, n, MOD) for c in row_combinations]
    
    # Adım 3: O(W^2)
    # Değişen genişlikteki N yüksekliğindeki bir duvar için kararsız duvar konfigürasyonlarının sayısını bul
    unstable = [0, 0]
    
    # Duvarı sol ve sağ kısma ayır,
    # ve sol kısmın ve sağ kısmın kombinasyonunu hesapla.
    # Genişlik 2'den başlayarak ihlal hakkında düşünmeye başlıyoruz.
    for i in range(2, m + 1):
        # i: mevcut toplam genişlik
        # j: sol genişlik
        # i - j: sağ genişlik
        # f: (sol kısım - önceki dikey ihlal)*sağ kısım
        f = lambda j: (total[j] - unstable[j]) * total[i - j]
        result = sum(map(f, range(1, i)))
        unstable.append(result % MOD)
    
    # Kararlı duvar kombinasyonlarının sayısını yazdır
    return (total[m] - unstable[m]) % MOD

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])
        m = int(first_multiple_input[1])

        result = legoBlocks(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()

