# İngilizce gazeteye abone olan öğrencilerin sayısı ve numaraları
n = int(input())
english_subscribers = set(map(int, input().split()))

# Fransızca gazeteye abone olan öğrencilerin sayısı ve numaraları
m = int(input())
french_subscribers = set(map(int, input().split()))

# İki kümenin birleşimini alarak toplam abone sayısını bulma
total_subscribers = english_subscribers.union(french_subscribers)

# En az bir gazeteye abone olan öğrencilerin toplam sayısını bulma
total = len(total_subscribers)

# Sonucu ekrana yazdırma
print(total)
