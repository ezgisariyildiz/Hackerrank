import re

# Kullanıcıdan girdi sayısını alıyoruz
for _ in range(int(input())):

    # Her bir metin satırını alıyoruz
    text = input()

    # Değiştirme işlemi için gerekli sembollerin ve yerine geçecek kelimelerin çiftleri
    replacements = [('\&\&', 'and'), ('\|\|', 'or')]

    # Her sembol çifti için değiştirme işlemini gerçekleştiriyoruz
    for symbol, replacement in replacements:
        # re.sub() fonksiyonu kullanılarak semboller değiştiriliyor
        # (?<= ) ve (?= ) kullanarak, sembollerin her iki yanında birer boşluk olduğundan emin olunur
        text = re.sub(r"(?<= )(" + symbol + ")(?= )", replacement, text)

    # Değiştirilmiş metin satırını yazdırıyoruz
    print(text)
