# M kümesinin eleman sayısını ve elemanlarını al
M_count = int(input())
M_elements = list(map(int,input().split()))

# N kümesinin eleman sayısını ve elemanlarını al
N_count = int(input())
N_elements = list(map(int,input().split()))

# M ve N kümelerini oluştur
M_set = set(M_elements)
N_set = set(N_elements)

# Simetrik farkı bul ve sırala
symmetric_difference = sorted(M_set.symmetric_difference(N_set))

# Her elemanı yazdır
for element in symmetric_difference:
    print(element)