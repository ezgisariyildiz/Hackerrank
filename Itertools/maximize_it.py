from itertools import product

K, M = map(int, input().split())

lists = []
for _ in range(K):
    ''' Her döngüde, boşluklarla ayrilmis olarak alinan girdinin
    ikinci satirindan başlayarak elemanlari alir 
    ve bunlari integer'a dönüştürerek lists listesine ekler'''
    lists.append(list(map(int, input().split()[1:])))

max_val = 0
# lists listesindeki her bir listenin elemanları arasından her bir kombinasyonu alır
for combination in product(*lists):
    # Her bir kombinasyonun elemanlarının karelerini alıp toplar ve M'ye göre modunu alarak denklemin sonucunu bulur
    s = sum(x ** 2 for x in combination) % M
    if s > max_val:
        max_val = s

print(max_val)