# ************ DAY4: MOCK TEST: TRUCK TOUR ************************


def truckTour(petrolpumps):
    # Petrol miktarını tutmak için değişken
    total_petrol = 0
    # Toplam mesafeyi tutmak için değişken
    total_distance = 0
    # Başlangıç petrol istasyounun indexi
    start_index = 0

    for i in range(len(petrolpumps)):
        # Mevcut petrol istasyonunun petrol ve mesafe bilgileri
        petrol, distance = petrolpumps[i]
        # Toplam petrol miktarına mevcut petrol istasyonunun petrol miktarını ekler
        total_petrol += petrol
        # Toplam mesafeye mevcut petrol istasyonunun mesafesini ekler
        total_distance += distance

        # Eğer mevcut petrol miktarı, mevcut mesafeden küçükse, bu istasyondan başlamak mümkün değildir.
        # Bu yüzden, başlangıç istasyonunu bir sonraki istasyona güncelleriz ve toplam petrol ve mesafeyi sıfırlarız.

        if total_petrol < total_distance:
            start_index = i + 1
            total_distance = 0
            total_petrol = 0

    return start_index