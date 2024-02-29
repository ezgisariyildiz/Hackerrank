# cube lambda ifadesini tanımlayalım
cube = lambda x: x **3

# fibonacci fonksiyonunu tanımlayalım
def fibonacci(n):
    # İlk iki fibonacci sayısı 0 ve 1 dir
    fib = [0, 1]
    # Fibonacci dizisini oluşturalım
    for i in range(2, n):
        fib.append(fib[i-1]+ fib[i-2])
        return fib[:n] # İlk n fibonacci sayısını döndürelim
    
if __name__ == '__main__':
    n = int(input()) # Kullanıcıdan N değerini alalım
    # Her bir Fibonacci sayısının küpünü alıp ekrana yazdırlaım
    print(list(map(cube, fibonacci(n))))