# A ve B kümesinin eleman sayılarını al
n, m = map(int, input().split())
arr = list(map(int, input().split()))

# Kullanıcının sevdiği ve sevmediği sayıları al
A = set(map(int,input().split()))
B = set(map(int, input().split()))

# Başlangıç mutluluğu
happiness = 0

# Kullanıcının mutluluğunu hesapla
for num in arr:
    # Eğer i A kümesindeyse, mutluluğu arttır
    if num in A:
        happiness += 1
    # Eğer i B kümesindeyse, mutluluğu azalt
    elif num in B:
        happiness -= 1

# Son mutluluğu yazdır
print(happiness)