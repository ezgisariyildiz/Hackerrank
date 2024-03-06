from collections import OrderedDict

# Kelime sayısı
n = int(input())
word_count = OrderedDict()

for _ in range(n):
    # Her kelimeyi oku
    word = input().strip()
    if word in word_count:
        # Sözcük zaten mevcutsa sayıyı artır
        word_count[word] += 1
    else:
     # Sözcükle ilk kez karşılaşılıyorsa sayımı başlat
        word_count[word] = 1

# Farklı kelimelerin sayısının çıktısı
print(len(word_count))

# Her farklı kelime için oluşum sayısını çıktı olarak verir
print(*word_count.values())
