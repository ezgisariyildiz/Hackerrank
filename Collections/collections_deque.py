from collections import deque
# Boş bir deque oluştur
d = deque()
# İşlem sayısını al
N = int(input())

# İşlemleri gerçekleştir
for _ in range(N):
    # İşlem adını ve değerini ayır
    operation, *args = input().split()
    if hasattr(d, operation): # Eğer deque üzerinde böyle bir işlem varsa
         # İlgili işlemi gerçekleştir
        getattr(d, operation)(*args)

# Deque'in elemanlarını yazdır
print(*d)