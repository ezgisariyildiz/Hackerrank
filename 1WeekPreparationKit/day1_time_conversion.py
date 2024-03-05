def timeConversion(s):
    # Saati, dakikayı, saniyeyi va AM/PM göstergesini ayıkla
    hour, minute, second = map(int, s[:-2].split(':'))
    period = s[-2:]

    # Zamanı 24 saatlik formata dönüştür
    if period == 'AM':
        if hour == 12:
            hour = 0
    else:
        if hour != 12:
            hour += 12

    # Saati 24 saatlik formatta formatla
    return '{:02d}:{:02d}:{02d}'.format(hour, minute, second)

# Girdiyi oku
s = input()

# timeConversion fonksiyonunu çağır ve sonucu yazdır
print(timeConversion(s))