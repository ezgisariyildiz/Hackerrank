def merge_the_tools(string, k):
    n = len(string)
    parts = [string[i:i+k] for i in range(0, n, k)]  # String'i parçalara ayır

    for part in parts:
        unique_chars = []
        for char in part:
            if char not in unique_chars:
                unique_chars.append(char)  # Tekil karakterleri bul
        print(''.join(unique_chars))  # Tekil karakterlerden oluşan string'i yazdır

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
