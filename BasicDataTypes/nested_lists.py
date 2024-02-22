if __name__ == '__main__':
    students = {}
    for _ in range(int(input().strip())):
        name = input().strip()
        score = float(input().strip())
        students[name] = score

    # Notları sırala ve ikinci en düşük notu bul
    sorted_scores = sorted(set(students.values()))
    second_lowest_score = sorted_scores[1]

    # İkinci en düşük notu alan öğrencileri bul
    second_lowest_students = [name for name, score in students.items() if score == second_lowest_score]

    # İsimleri alfabetik sıraya göre sırala
    second_lowest_students.sort()

    # İsimleri yazdır
    for student in second_lowest_students:
        print(student)
