from fractions import Fraction
from functools import reduce

def product(fracs):
    # reduce() fonksiyonunu kullanarak tüm rasyonel sayıların çarpımını hesaplayın
    t = reduce(lambda x, y: x * y, fracs)
    # Hesaplanan çarpımın pay ve payda değerlerini döndürürür
    return t.numerator, t.denumerator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        # Her rasyonel sayı için kullanıcıdan girdi alırız, bu girdiyi ikiye böleriz ve Fraction sınıfı kullanarak rasyonel sayı oluşturur
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)