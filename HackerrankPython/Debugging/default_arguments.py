# Çift sayıları üreten bir sınıf oluşturduk
class EvenStream(object):
    def __init__(self):
        self.current = 0   # Başlangıç değeri

    # Bir sonraki çift sayıyı getiren method
    def get_next(self):
        to_return = self.current # Mevcut değeri döndürür
        self.current += 2   # Bir sonraki çift sayıya geç
        return to_return
    
# Tek sayıları üreten bir sınıf oluşturduk
class OddStream(object):
    def __init__(self):
        self.current = 1   # Başlangıç değeri

    # Bir sonraki tek sayıyı getiren method
    def get_next(self):
        to_return = self.current   # Mevcut değeri döndürür
        self.current += 2  # Bir sonraki tek sayıya geç
        return to_return
    
# Akıştan belirli sayıda elemanları yazdıran fonksiyon
def print_from_stream(n, stream=EvenStream()): # Varsayılan akış EvenStream dir
    stream.__init__()   # Akışı yeniden başlat
    for _ in range(n):  # Belirtilen sayıda eleman yazdır
        print(stream.get_next())  # Akıştan bir sonraki elemanı al ve yazdır

# Girişten sorgu sayısını oku
queries = int(input())
# Her bir sorgu için
for _ in range(queries):
    # Akış adı ve sayıyı oku
    stream_name, n = input().split()
    n = int(n) # tamsayıya dönüştür
    # Eğer akış adı "even" ise 
    if stream_name == "even":
        print_from_stream(n) # Belirtilen sayıda çift sayıyı yazdır
    else:
        # Değilse, OddStream kullanarak belirtilen sayıda tek sayıyı yazdır
        print_from_stream(n, OddStream())
