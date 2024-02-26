# İlk sayıyı oku
a = int(input().strip())

# İkinci sayıyı oku
b = int(input().strip())

# Bölümü ve kalanı hesapla
quotient = a // b
remainder = a % b

# divmod() fonksiyonunu kullanarak bölümü ve kalanı hesapla
divmod_result = divmod(a, b)

# Sonuçları yazdır
print(quotient)
print(remainder)
print(divmod_result)
