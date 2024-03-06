import re

# Düzenli ifadeleri tanımlayın
regex_integer_in_range = r"^[1-9][0-9]{5}$" # [100000, 999999] aralığında bir sayıyı eşleştirir
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)" # Sırasıyla tekrar eden rakam çiftlerini eşleştirir

# Giriş posta kodunu okuyun
P = input()

# Posta kodunun her iki koşulu da karşılayıp karşılamadığını kontrol edin
valid_postal_code = bool(re.match(regex_integer_in_range, P)) and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2

# Sonucu (True veya False) yazdırın
print(valid_postal_code)