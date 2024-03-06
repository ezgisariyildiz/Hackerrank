import math

AB = float(input().strip())
BC = float(input().strip())

# Hipotenüsü (AC) Pisagor Teoremi ile bulunur
AC = math.sqrt(AB**2 + BC**2)

# MAB açısını (θ) bulmak için arccos fonksiyonunu kullanın
theta = math.acos(BC / AC)

# Radyan cinsinden thetayı dereceye çevirin
MAC = math.degrees(theta)

# Derece sembolünü içeren çıktıyı oluşturun
output = str(round(MAC)) + "\u00b0"

# Sonucu ekrana yazdırın
print(output)