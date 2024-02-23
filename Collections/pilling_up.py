from collections import deque

# Test durumlarının sayısını alalımm
T = int(input())

# Her bir test durumu için 
for _ in range(T):
    # Küp sayısını ve yan uzunlukları alalım
    n = int(input())
    side_lengths = list(map(int, input().split()))

    # Yığını oluşturmak için bir deque kullanalım
    pile = deque(side_lengths)

    # Önceki küpün yan uzunluğunu tutmak için bir değişken tanımlayalım
    prev_side_length = float('inf')

    # Her bir küp için
    for _ in range(n):
        # En büyük yan uzunluğa sahip olanı seçelim
        current_side_length = max(pile[0], pile[-1])

        # Eğer önceki küpten daha küçük bir yan uzunluğa sahipse
        if current_side_length <= pile[-1]:
            # Stack in solundan veya sağından bir eleman çıkaralım
            if pile[0] >= pile[-1]:
                pile.popleft()
            else:
                pile.pop()
            # Önceki küpün yan uzunluğunu güncelleyelim
            prev_side_length = current_side_length
        # Eğer bu koşul sağlanmazsa, stack i oluşturamayız
        else:
            print("No")
            break
    else:
        # Her şey yolundaysa, stack i oluşturabiliriz
        print("Yes")
    