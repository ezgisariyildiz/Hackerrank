from datetime import datetime
import os

# Complete the time_delta function below.
def time_delta(t1, t2):
    # Zaman damgalarını ayrıştırır ve datetime nesnelerine dönüştürür
    t1 = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    t2 = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')

    # Zaman farkını hesaplar (mutlak değer olarak)
    diff = abs(t2 - t1)

    # Farkı saniye cinsine dönüştürür ve string olarak döndürür
    return str(int(diff.total_seconds()))

if __name__ == '__main__':
    # Çıktı dosyasını açar ve yazma modunda ayarlar
    fptr = open(os.environ['OUTPUT_PATH'], 'w')  

    t = int(input())  # Test sayısını alır

    # Her test için tekrarlar
    for t_itr in range(t):
        t1 = input()  # İlk zaman damgasını alır
        t2 = input()  # İkinci zaman damgasını alır

        delta = time_delta(t1, t2)  # Zaman farkını hesaplar

        fptr.write(delta + '\n')  # Zaman farkını çıktı dosyasına yazar

    fptr.close()  # Çıktı dosyasını kapatır
