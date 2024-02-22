if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    # Verilen öğrencinin notlarını al
    scores = student_marks[query_name]

    # Ortalamayı hesapla
    avg_score = sum(scores) / len(scores)

    # Sonucu yazdır
    print("{:.2f}".format(avg_score))
