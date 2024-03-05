def plusMinus(arr):
    # Dizinin boyutunu alın
    n = len(arr)
    
    # Pozitif, negatif ve sıfır değerlerin sayısını başlatın
    positive_count = 0
    negative_count = 0
    zero_count = 0
    
    # Diziyi dolaşarak pozitif, negatif ve sıfır sayılarını sayın
    for num in arr:
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1
        else:
            zero_count += 1
    
    # Pozitif, negatif ve sıfır değerlerin oranlarını hesaplayın
    positive_ratio = positive_count / n
    negative_ratio = negative_count / n
    zero_ratio = zero_count / n
    
    # Sonuçları altı ondalık basamağa kadar yazdırın
    print("{:.6f}".format(positive_ratio))
    print("{:.6f}".format(negative_ratio))
    print("{:.6f}".format(zero_ratio))

# Girişten dizi boyutunu alın
n = int(input())

# Diziyi alın ve uzayla ayrılmış tamsayılar listesine dönüştürün
arr = list(map(int, input().split()))

# plusMinus fonksiyonunu çağırarak sonuçları yazdırın
plusMinus(arr)
