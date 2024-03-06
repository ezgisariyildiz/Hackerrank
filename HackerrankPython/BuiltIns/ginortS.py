# Verilen string S yi alıyoruz
S = input()

# S yi sıralıyoruz ve anahtar fonksiyonu olark kullanılacak öncelik sırasını belirtiyoruz
sorted_s = sorted(S, key=lambda x: (x.isdigit(), x.isdigit() and int(x) % 2 == 0, x.isupper(), x))

# Sıralı listeyi birleştirerek sonucu elde ediyoruz
result = ''.join(sorted_s)

# Sonucu yazdırıyoruz
print(result)

