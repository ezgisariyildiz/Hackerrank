def sort_athletes(athletes, K):
    # Sporcuları K. niteliğe göre sıralayın
    sorted_athletes = sorted(athletes, key=lambda x: x[K])
    return sorted_athletes

if __name__ == '__main__':
    # Sporcu sayısını (N) ve nitelik sayısını (M) girin
    N, M = map(int(), input().split())

    # Her sporcunun ayrıntılarını girin
    athletes = [list(map(int(), input().split())) for _ in range(N)]

    # Sıralanacak özniteliği girin (K)
    K = int(input())

    # Sporcuları K. niteliğe göre sıralayın
    sorted_athletes = sorted(athletes, key=lambda x: x[K])

    # Sıralanmış tabloyu yazdır
    for athlete in sorted_athletes:
        print(*athlete)