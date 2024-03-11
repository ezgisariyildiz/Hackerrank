import heapq

def cookies(k, A):
    # Kurabiyeleri heap olarak sıralayın
    heapq.heapify(A)
    
    operations = 0  # İşlem sayacı
    while len(A) >= 2 and A[0] < k:
        # En düşük tatlılık seviyesine sahip iki kurabiye alın
        min1 = heapq.heappop(A)
        min2 = heapq.heappop(A)

        # Yeni birleştirilmiş kurabiye tatlılık seviyesini hesaplayın
        new_cookie = min1 + 2 * min2

        # Yeni kurabiyeyi heap'e ekleyin
        heapq.heappush(A, new_cookie)

        # Birleştirme işlemi yapıldı, işlem sayacını artırın
        operations += 1

    # Tüm kurabiyelerin tatlılık seviyesi K veya daha büyükse, işlem sayısını döndürün
    if A and A[0] >= k:
        return operations
    else:
        return -1

if __name__ == '__main__':
    # input alınır
    n, k = map(int, input().rstrip().split())  # Kurabiye sayısı ve hedef tatlılık seviyesi
    A = list(map(int, input().rstrip().split()))  # Kurabiyelerin tatlılık seviyeleri

    result = cookies(k, A)  # cookies fonksiyonunu çağırarak işlem sayısını hesapla

    # Sonuç yazdırılır
    print(result)
