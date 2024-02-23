# Test sayısını al
T = int(input())

# Her bir test durumu için
for _ in range(T):
    # A setini ve elemanlarını al
    input()
    A = set(map(int, input().split()))

    # B setini ve elemanlarını al
    input()
    B = set(map(int, input().split()))

    # A seti B nin alt kümesi mi kontrol et
    if A.issubset(B):
        print(True)
    else:
        print(False)