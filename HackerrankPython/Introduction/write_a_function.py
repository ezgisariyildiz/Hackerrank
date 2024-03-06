def is_leap(year):
    leap = False
    
    if year%4==0:
        leap = True
        if year%100==0:
            leap = False
            if year%400==0:
                leap = True
            
    return leap

year = int(input())
print(is_leap(year))

##############İkinci yol#################

def is_leap(year):
    if year % 4 == 0:  # Yıl 4'e tam bölünüyorsa
        if year % 100 == 0:  # Yıl aynı zamanda 100'e tam bölünüyorsa
            if year % 400 == 0:  # Yıl 400'e de tam bölünüyorsa
                return True  # Artık yıldır
            else:
                return False  # Artık yıl değildir
        else:
            return True  # Artık yıldır
    else:
        return False  # Artık yıl değildir
