# Ortalamaları hesaplamak için bir işlev tanımlayın
def avage_marks(*subjects):
    # Öğrenci sayısını hesaplayın 
    num_students = len(subjects[0])

    # Her öğrenci üzerinde yinele 
    for i in range(num_students):
        # Geçerli öğrenci için notların toplamını hesaplayın
        total_marks = sum(subject[i] for subject in subjects)

        # Mevcut öğrenci için ortalama notları hesaplayın  
        average = total_marks / len(subjects)

        # Mevcut öğrenci için ortalama notları yazdır
        print("{:.1f}".format(average))

# Öğrenci ve denek sayısını girin
N, X = map(int, input().split())

# Tüm öğrenciler için her ders için giriş notları
marks = [list(map(float, input().split())) for _ in range(X)]

# Her öğrenci için ortalama notları hesaplamak ve yazdırmak için işlevi çağırın
avage_marks(*marks)