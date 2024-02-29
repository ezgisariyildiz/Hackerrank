import re

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = input()
        # Bu desen, ondalık bir sayıyı tanımlar.
        pattern = r'^[-+]?\d*\.\d+$'
        # re.match() fonksiyonunu kullanarak desen eşleştirmesi yaparız.
        # Eğer eşleşme başarılıysa, yani girdi ondalık bir sayı ise, True çıktısı veririz
        if re.match(pattern, N):
            print(True)
        else:
            print(False)


# ^ : Dizinin başlangıcını belirtir.
# [-+]? : İsteğe bağlı bir işaret (- veya +).
# \d* : 0 veya daha fazla rakam.
# \. : Ondalık nokta.
# \d+ : En az bir rakam.
# $ : Dizinin sonunu belirtir.