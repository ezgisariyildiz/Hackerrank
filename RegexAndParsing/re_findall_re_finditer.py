import re

def find_vowel_substrings(s):
    # En az 2 sesli harf içeren alt dizeleri bulmak için regex kalıbı
    pattern = r'(?<=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])[aeiouAEIOU]{2,}(?=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])'
    
    # Desenle eşleşen tüm alt dizeleri bul
    substrings = re.findall(pattern, s)
    
    # Eşleşen alt dizeleri yazdır
    if substrings:
        for substring in substrings:
            print(substring)
    else:
        print(-1)

if __name__ == "__main__":
    s = input()
    find_vowel_substrings(s)
