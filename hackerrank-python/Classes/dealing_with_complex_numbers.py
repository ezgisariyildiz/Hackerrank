import math

class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        return Complex(self.real + no.real, self.imaginary + no.imaginary)

    def __sub__(self, no):
        return Complex(self.real - no.real, self.imaginary - no.imaginary)

    def __mul__(self, no):
        return Complex(
            self.real * no.real - self.imaginary * no.imaginary,
            self.real * no.imaginary + self.imaginary * no.real,
        )

    def __truediv__(self, no):
        divider = no.real**2 + no.imaginary**2
        return Complex(
            (self.real * no.real + self.imaginary * no.imaginary) / divider,
            (self.imaginary * no.real - self.real * no.imaginary) / divider,
        )

    def mod(self):
        return Complex(math.sqrt(self.real**2 + self.imaginary**2), 0.00)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')

'''
Complex sinifi tanimlanir. 
Bu siniff, karmasik sayilari temsil etmek için kullanilir. 
real ve imaginary olmak üzere iki özellik içerir. 
real, karmaşik sayinin gerçel kismini, imaginary ise sanal kismini temsil eder.
__add__ metodu, iki karmaşik sayiyi toplar. 
Yeni bir Complex nesnesi döndürür ve bu nesnenin gerçel ve sanal kisimlari, 
toplami alinan iki karmaşik sayinin gerçel ve sanal kisimlarinin toplamidir.

__sub__ metodu, iki karmaşik sayi arasindaki farki hesaplar. 
Yine yeni bir Complex nesnesi döndürür ve bu nesnenin gerçel ve sanal kisimlari, 
çikarilan iki karmasik sayinin gerçel ve sanal kisimlarinin farkidir.

__mul__ metodu, iki karmaşik sayinin çarpimini hesaplar. 
Yine yeni bir Complex nesnesi döndürür ve bu nesnenin gerçel ve sanal kisimlari, 
çarpilan iki karmaşik sayinin gerçel ve sanal kisimlarinin çarpimidir.

__truediv__ metodu, bir karmaşik sayiyi diğerine böler. 
Yine yeni bir Complex nesnesi döndürür ve bu nesnenin gerçel ve sanal kisimlari, 
bölünen karmaşik sayinin gerçel ve sanal kisimlarinin bölümüdür.

mod metodu, bir karmaşik sayinin modülünü hesaplar. 
Bu metot, math.sqrt() fonksiyonunu kullanarak karmaşik sayinin modülünü hesaplar. 
Ancak, gerçek ve sanal kisimlarin karesinin toplami şeklinde bir sonuç döndürür.

__str__ metodu, bir karmaşik sayinin metin temsilini oluşturur. 
Önce karmaşik sayinin gerçel ve sanal kisimlarina göre uygun bir metin oluşturulur. 
Sonra bu metin döndürülür.

Ana program kismi, Complex sinifini kullanarak kullanicidan girdileri alir, 
bu girdileri karmaşik sayi nesnelerine dönüştürür ve belirli işlemleri gerçekleştirir. 
Sonuçlari ekrana yazdirir.
'''