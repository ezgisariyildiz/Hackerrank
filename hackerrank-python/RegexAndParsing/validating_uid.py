import re

def is_valid_uid(uid):
    # Kural 1: En az 2 büyük harfli içeren İngilizce alfabe karakteri
    if len(re.findall(r'[A-Z]', uid)) < 2:
        return False
    
    # Kural 2: En az 3 rakam içermeli (0 - 9)
    if len(re.findall(r'\d', uid)) < 3:
        return False
    
    # Kural 3: Yalnızca alfanümerik karakterler (a - z, A - Z & 0 - 9)
    if not uid.isalnum():
        return False
    
    # Kural 4: Hiçbir karakter tekrar etmemeli
    if len(set(uid)) != len(uid):
        return False
    
    # Kural 5: Tam olarak 10 karakterden oluşmalı
    if len(uid) != 10:
        return False
    
    return True

if __name__ == '__main__':
    t = int(input().strip())
    for _ in range(t):
        uid = input().strip()
        if is_valid_uid(uid):
            print("Valid")
        else:
            print("Invalid")
