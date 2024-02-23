import statistics

def average(array):
    # Dizideki benzersiz yükseklikleri bulmak için dizi elemanlarını bir küme veri yapısına dönüştürür.
    distinct_heights = set(array)
    
    # Benzersiz yüksekliklerin toplamını alır ve bu toplamı kümenin eleman sayısına böler. Bu, kümenin ortalamasını hesaplar.
    avg_heights = sum(distinct_heights) / len(distinct_heights)
    
    # Ortalama değeri yuvarlar ve üç ondalık basamağa kadar kesirli kısmı korur.
    # Son olarak, bu yuvarlanmış ortalama değeri döndürür.
    return round(avg_heights, 3)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
