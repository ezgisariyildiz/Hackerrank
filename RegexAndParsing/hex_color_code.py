import re

# Kullanıcıdan CSS kod satırlarının sayısını alın
num_lines = int(input())

# CSS kodlarını birleştirmek için boş bir string oluşturun
css = ""

# Kullanıcıdan CSS kodlarını alın ve birleştirin
for _ in range(num_lines):
    css += input()

# Her bir stil bloğunu(süslü parantezler arasındaki kısmı) bulmak için re.findall() kullan
for match in re.findall(r"\{[^\}]*\}", css):
    # Her stil bloğundan renk kodlarını(HEX formatında) bulmak için re.findall() kullan
    color_codes = re.findall(r"(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})", match)
    # Her bir renk kodunu yazdır
    for color_code in color_codes:
        print(color_code)