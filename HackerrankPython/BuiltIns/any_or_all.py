def is_palindrome(n):
    # Bir sayının palindromik olup olmadığını kontrol eden fonksiyon
      # 1234 ==> 4321
    return str(n) == str(n)[::-1]

if __name__ == '__main__':
    # Input alınır
    # N = listenin eleman sayısı
    N = int(input())
    # Listenin elemanları alınır
    numbers = list(map(int, input().split()))

    # Tüm sayıların pozitif olup olmadığının kontrol edilmesi
    all_positive = all(num > 0 for num in numbers)

    # Eğer tüm sayılar poziifse, herhangi bir sayının palindromik olup olmadığının kontrol edilmesi
    if all_positive:
        any_palindrome = any(is_palindrome(num) for num in numbers)
        print(any_palindrome)
    else:
        print(False)
