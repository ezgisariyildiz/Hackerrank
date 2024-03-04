for i in range(1, int(input())+ 1):
    # 2 satırdan fazlası 0 puanla sonuçlanacaktır. Boş satır da bırakmayın!!
    print(((10**i - 1) // 9) ** 2)