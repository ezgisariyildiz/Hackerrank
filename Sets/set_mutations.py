# Ana kümenin elemanlarını al
n = int(input())
s = set(map(int, input().split()))

# Diğer setlerin sayısını al
num_other_sets = int(input())

# Diğer setler ve operasyonları alarak işlemleri uygula
for _ in range(num_other_sets):
    operation, length = input().split()
    other_set = set(map(int, input().split()))
    
    # Operasyonları uygula
    if operation == 'intersection_update':
        s.intersection_update(other_set)
    elif operation == 'update':
        s.update(other_set)
    elif operation == 'difference_update':
        s.difference_update(other_set)
    elif operation == 'symmetric_difference_update':
        s.symmetric_difference_update(other_set)

# Sonuç kümesindeki elemanların toplamını yazdır
print(sum(s))