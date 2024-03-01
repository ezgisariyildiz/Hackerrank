import re

# Matris boyutlarını ve satırlarını alın
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

# Sütunları gezerek alfanümerik karakterleri birleştirin
    decoded_script = ''.join(matrix[j][i] for i in range(m) for j in range(n))

    # Alfanümerik olmayan karakterlerin ve boşlukların arasına tek bir boşluk karakteri ekleyin
    decoded_script = re.sub(r'(?<=\w)([^\w\d]+)(?=\w)', ' ', decoded_script)

    # Çözülmüş matrisi yazdırın
    print(decoded_script)