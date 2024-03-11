#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

def cookies(k, A):
    # Önce, Jesse'nin tüm kurabiyelerinin tatlılık seviyelerini kontrol etmemiz gerekiyor.
    # Jesse, birleştirerek en az iki kurabiyenin tatlılık seviyelerini artırarak birleştirir.
    # Bu işlemi tekrarlayarak tüm kurabiyelerin tatlılık seviyelerini K'ye eşit veya büyük hale getirmeye çalışırız.
    # İlk adım olarak, kurabiyeleri tatlılık seviyesine göre sıralarız.

    A.sort()  # Kurabiyeleri sırala

    operations = 0  # İşlem sayacı
    while len(A) >= 2 and A[0] < k:
        # Eğer en düşük tatlılık seviyesine sahip kurabiye, K'den küçükse ve koleksiyonda en az 2 kurabiye varsa,
        # bu durumda birleştirme işlemi yapılması gerekmektedir.

        # En düşük tatlılık seviyesine sahip iki kurabiye birleştirilir.
        combined_cookie = A[0] + 2 * A[1]

        # Yeni birleştirilmiş kurabiye koleksiyona eklenir.
        A.pop(0)  # En düşük tatlılık seviyesine sahip kurabiye koleksiyondan çıkarılır.
        A.pop(0)  # İkinci en düşük tatlılık seviyesine sahip kurabiye koleksiyondan çıkarılır.
        A.append(combined_cookie)  # Yeni birleştirilmiş kurabiye koleksiyona eklenir.

        # Yapılan birleştirme işlemi sayısını arttırılır.
        operations += 1

        # Kurabiyeleri tekrar sıralayarak en düşük tatlılık seviyesine sahip kurabiyeyi yeniden belirleriz.
        A.sort()

    # Sonuç olarak, tüm kurabiyelerin tatlılık seviyeleri K'ye eşit veya büyükse,
    # yapılan toplam işlem sayısını döndürürüz.
    # Aksi takdirde, işlemin mümkün olmadığını belirtmek için -1 döndürülür.
    if A and A[0] >= k:
        return operations
    else:
        return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])  # Kurabiye sayısı
    k = int(first_multiple_input[1])  # Minimum tatlılık seviyesi

    A = list(map(int, input().rstrip().split()))  # Kurabiyelerin tatlılık seviyeleri

    result = cookies(k, A)  # cookies fonksiyonunu çağırarak işlem sayısını hesapla

    fptr.write(str(result) + '\n')  # Sonucu dosyaya yaz

    fptr.close()  # Dosyayı kapat
