def minimumBribes(q):
    # Verilen diziyi sıfırdan başlayarak indexlemek için her elemnadan 1 çıkarıyoruz
    q = [i-1 for i in q]
    # Toplam rüşvet sayısını tutacak değişken
    bribes = 0

    # Her kişi için sırasını kontrol eder
    for i, o in enumerate(q):
        # Mevcut kişinin indexini tutar
        cur = i

        # Eğer kişinin beklendiği sıradan 2 veya daha fazla ileride ise "Too Chaotic" yazdr
        if o - cur > 2:
            print("Too chaotic")
            return
        
        # Kişinin beklediği sıradan bir önceki indexten ( maksimum olarak sıfır) mevcut kişinin indexine kadar olan aralıktaki kişileri kontrol eder
        for k in q[max(o - 1, 0):i]:
            # Eğer bu kişi, beklenen kişiden daha büyük bir sıradaysa, bir rüşvet alındığını belirtir ve rüşvet sayısını artırır
            if k > o:
                bribes += 1

    # Toplam rüşvet sayısını yazdırır
    print(bribes)

if __name__ == '__main__':
    t = int(input().strip())  # Test durum sayısını alır

    # Her bir test durumu için girişleri alır ve minimumBribes fonksiyonunu çağırır
    for t_itr in range(t):
        n = int(input().strip())  # Kişi sayısını alır

        q = list(map(int, input().rstrip().split()))  # Kişilerin sıra bilgilerini alır

        minimumBribes(q)  # Minimum rüşvet sayısını hesaplamak için minimumBribes fonksiyonunu çağırır
     