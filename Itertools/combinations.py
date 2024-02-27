from itertools import combinations

# Girişleri al
s, k = input().split()

# S stirnginin içindeki kombinasyonları (k-1 e kadar) hesaplar
# Her bir kombinasyonun elemanlarını alfabetik sıraya göre sıralamak için map fonksiyonu kullanılır. 
# lambda x: sorted(x) ifadesi, her bir kombinasyon için elemanları sıralayan bir lambda fonksiyonunu temsil eder.
for i in range(int(k)):
    [print(''.join(p)) for p in sorted(map(lambda x: sorted(x), combinations(s, i + 1)))] 