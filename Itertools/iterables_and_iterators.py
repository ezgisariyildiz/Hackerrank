from itertools import combinations

n = int(input())
s = input().split()
k = int(input())

combs = list(combinations(s, k))

# combs listesinde dolaşarak, her bir kombinasyon içinde 'a' harfinin olup olmadığını kontrol eder. 
# 'a' harfi içeren kombinasyonların sayısını hesaplar ve bu sayıyı has_a değişkenine atar.
has_a = sum(1 for c in combs if 'a' in c)

#  'a' harfinin içme olasılığını hesaplamak için 'a' harfi içeren kombinasyonların 
# toplam kombinasyon sayısına oranını hesaplar ve sonucu ekrana yazdırır.
print(has_a / len(combs))