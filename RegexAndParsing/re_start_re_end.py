import re

# s işlem yapılacak ana dize, 
s = input()
# k ise altdizeyi temsil eder
k = input()

# re.finditer() fonksiyonunu kullanarak s içinde k alt dizesinin tüm eşleşmelerini buluyoruz. 
# Bu fonksiyon, eşleşmelerin başlangıç indislerini içeren bir eşleşme nesneleri listesi döndürür.
matches = list(map(lambda x: x, re.finditer(r"(?=%s)" % k, s)))

# En az bir eşleşme bulunmuşsa, eşleşmelerin başlangıç ve bitiş indislerini ekrana yazdırmak için bir döngüye girer
if matches:
    for m in matches:
        for m in matches:
            #  her bir eşleşme için başlangıç ve bitiş indislerini ekrana yazdırır
            print((m.start(), m.start() + len(k) - 1))
# Eğer matches listesi boşsa, yani hiçbir eşleşme bulunamamışsa, -1 yazdırır
else:
    print(-1)