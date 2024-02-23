# Karakterlerin sayısını hesaplamak için bir fonksiyon tanımlıyoruz.
def count_chars(s):
    # Her bir karakterin sayısını tutacak bir sözlük oluşturuyoruz.
    char_count = {}
    
    # Döngü ile dizedeki her bir karakteri alıyoruz.
    for char in s:
        # Karakterin sayısını artırmak için get() metodu kullanılır.
        # Eğer karakter zaten sözlükte varsa, sayısını artırırız.
        # Eğer yoksa, yeni bir anahtar oluşturarak sayıyı 1 yaparız.
        char_count[char] = char_count.get(char, 0) + 1
    
    # Karakterlerin sayısını içeren sözlüğü döndürüyoruz.
    return char_count

# Ana program akışı
if __name__ == '__main__':
    # Kullanıcıdan bir dize alıyoruz.
    s = input()
    
    # count_chars fonksiyonunu kullanarak karakterlerin sayısını hesaplıyoruz.
    char_count = count_chars(s)
    
    # Karakterlerin sayısını, sayılarına göre sıralayarak ilk üçünü alıyoruz.
    sorted_char_count = sorted(char_count.items(), key=lambda x: (-x[1], x[0]))[:3]
    
    # En sık geçen üç karakteri ve sayılarını ekrana yazdırıyoruz.
    for char, count in sorted_char_count:
        print(char, count)
