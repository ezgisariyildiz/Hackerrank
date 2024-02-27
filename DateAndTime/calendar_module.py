import calendar

# Girişleri al
month, day, year = map(int, input().split())

# Verilen tarihe göre haftanın hangi günü olduğunu bul
weekday = calendar.weekday(year, month, day)

# Gün ismini büyük harflerle yazdır
print(calendar.day_name[weekday].upper())