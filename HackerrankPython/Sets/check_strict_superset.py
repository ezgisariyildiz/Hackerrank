# A setini al
A = set(map(int, input().split()))

# Diğer N setlerini ve elemanlarını al
N = int(input())
sets = [set(map(int, input().split())) for _ in range(N)]

# A nın her bir N setinin katı olup olmadığını kontrol et
result = all(A.issuperset(s) for s in sets)

# Sonucu yazdır
print(result)