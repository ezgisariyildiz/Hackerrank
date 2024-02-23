from collections import Counter

# K değerini ve odalar listesini al
K = int(input())
rooms = input().split()

# Oda numaralarının sayısımı say
room_counts = Counter(rooms)

# Tekrarlanmayan oda numarasını bul
for room, count in room_counts.items():
    if count == 1:
        print(room)
        break