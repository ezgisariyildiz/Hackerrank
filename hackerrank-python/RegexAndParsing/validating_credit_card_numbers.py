import re

# Her bir kredi kartı numarası için işlem yapılır
for _ in range(int(input())):

    # Kredi kartı numarası alınır
    cc = input()

    # Kredi kartı numarası formatına uygun olup olmadığı kontrol edilir
    if re.search(r"^([456]\d{3})([ -]?\d{4}){3}$", cc):

        # Kredi kartı numarasındaki tüm non-digit karakterler kaldırılır
        cc = re.sub(r"[^\d]", "", cc)

        # Kredi kartı numarasında ardışık 4 veya daha fazla tekrar eden rakamların olup olmadığı kontrol edilir
        # Eğer yoksa kredi kartı numarası valid dir
        print('Valid' if not re.search(r'(\d)\1{3}', cc) else 'Invalid')

    # Kredi kartı numarası formatına uygun değilse, invalid dir
    else:
        print('Invalid')