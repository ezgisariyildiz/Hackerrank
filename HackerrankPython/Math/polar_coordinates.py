import cmath

# Karmaşık sayıyı kullanıcıdan giriş olarak alın
z = complex(input().strip())

# Karmaşık sayıyı polar koordinatlara dönüştürün
r, phi = cmath.polar(z)

# Polar koordinatları yazdırın
print(r)
print(phi)