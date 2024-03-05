import math
import os
import random
import re
import sys

# Aşağıdaki fonksiyon yanlızca bir kez geçen sayıyı bulmak için kullanılır
def lonely_integer(a):
    # Her bir sayının kaç kez geçtiğini takip etmek için bir sözlük oluşturuyoruz.
    count_dict = {}

    # Diziyi tara ve her bir sayının kaç kez geçtiğini say
    for num in a:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    # Tekrarlanmayan yani değeri 1 olan sayıyı bul
    for key, value in count_dict.items():
        if value == 1:
            return key
    
if __name__ =='__main__':
    # Çıktıyı bir dosyaya yazdırmak için dosya aç
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    # Kullanıcıdan dizinin boyutunu al
    n = int(input().strip())

    # Kullanıcıdan diziyi alıyoruz ve integer a dönüşütürüyoruz
    a = list(map(int,input().rstrip().split()))

    # lonelyinteger fonksiyonunu çağır
    result = lonely_integer(a)

    # Sonucu dosyayay yazdır
    fptr.write(str(result) + '\n')

    fptr.close()