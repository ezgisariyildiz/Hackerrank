import os

def superDigit(n, k):
    # Eğer n sadece bir basamaklıysa, super digit i n dir
    if len(n) == 1:
        return int(n)
    
    # Sayının her bir basamağını toplar
    digit_sum = sum(int(digit) for digit in n)

    # Elde edilen toplamın super digit ini hesaplamak için fonksiyonu tekrar çağır
    return superDigit(str(digit_sum * k), 1) # Yeni n değeri toplamın k kadar tekrar edilmiş hali olacak

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    print(str(result) + '\n')