import re

# Kullanıcıdan bir giriş alır ve bu girdideki deseni arar
m = re.search(r"(?P<repeat>([a-z0-9])\2?(?:\2))+", input())

# Eğer eşleşme bulunursa, bulunan karakterleri yazdırır.
# Eğer eşleşme bulunmazsa, -1 yazdırır
print(m.groupdict()['repeat'][0] if m else '-1')



'''
(?P<repeat>...): Adlandırılmış bir grup oluşturur. Bu grup repeat adını alır.
([a-z0-9]): Bir alfasayısal karakter veya rakamı eşleştirir. İlk karakteri temsil eder.
\2?: İkinci karakterle eşleşir, ancak bu karakterin olup olmamasına izin verir (?). Bu, ardışık tekrar eden karakterlerin bulunmasına yardımcı olur.
(?:\2): İkinci karakterin bir tekrarını eşleştirir.
+: Grubun bir veya daha fazla tekrarını eşleştirir. Bu, ardışık olarak tekrar eden karakterlerin bulunmasını sağlar.
'''

'''
m.groupdict(): Eşleşen grubun adlandırılmış gruplarını içeren bir sözlük döndürür.
['repeat']: 'repeat' anahtarını kullanarak, repeat adındaki grubu seçeriz.
[0]: Grubun ilk öğesini alırız. Çünkü repeat adındaki grup, eşleşen karakterlerin tamamını içerir. İlk öğe, ardışık olarak tekrar eden karakterlerin başlangıcını temsil eder.
if m else '-1': Eğer eşleşme bulunmazsa, -1 yazdırırız. Bu, re.search() fonksiyonunun geri dönüş değerinin None olup olmadığını kontrol eder. Eğer m değeri None ise, yani eşleşme yoksa, -1 yazdırılır.
'''