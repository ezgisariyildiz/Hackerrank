from itertools import groupby

# Girişi al
S = input()

# Değiştirilmiş stringi oluştur
modified_string = ''
for key, group in groupby(S):
    modified_string += f"({len(list(group))}, {key})"

# Sonucu yazdır
print(modified_string.rstrip())