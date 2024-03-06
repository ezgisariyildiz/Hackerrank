import math

# Points adında bir sınıf tanımlar. 
# Bu sınıf, 3-boyutlu uzaydaki noktaları temsil etmek için kullanılacaktır.
class Points(object):
    # Points sınıfının yapıcı metodunu tanımlar. 
    # Bu metod, bir noktanın x, y ve z koordinatlarını alır ve sınıfın özelliklerine (x, y ve z) atar.
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    # Points sınıfında "-" operatörünün davranışını tanımlar. 
    # Bu, iki nokta arasındaki farkı hesaplamak için kullanılır.
    def __sub__(self, no):
        return Points(self.x - no.x, 
                      self.y - no.y, 
                      self.z - no.z)
    
    # Points sınıfında iki vektör arasındaki dot product'u hesaplamak için bir metod tanımlar.
    def dot(self, no):
        return self.x * no.x + self.y * no.y + self.z * no.z

    # Points sınıfında iki vektör arasındaki cross product'u hesaplamak için bir metod tanımlar.
    def cross(self, no):
        return Points(self.y * no.z - self.z * no.y, 
                      self.z * no.x - self.x * no.z,
                      self.x * no.y - self.y * no.z)
    
    # Points sınıfında bir vektörün mutlak değerini hesaplamak için bir metod tanımlar.
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)
    

if __name__ == '__main__':
    # Bu liste, dört noktanın koordinatlarını depolamak için kullanılacaktır.
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])

    # `Points` sınıfından dört farklı nesne oluşturur. Her bir nesne, kullanıcıdan alınan dört noktanın koordinatlarını temsil eder.
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    
    # İki vektör oluşturur: AB x BC ve BC x CD.
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))
    
    # İki vektör arasındaki açıyı hesaplar.
    print("%.2f" % math.degrees(angle))