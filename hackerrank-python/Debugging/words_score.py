def score_words(words):
    score = 0
    vowels = "aeiouy" # Sesli harfleri temsil eden bir dize

    for word in vowels:
        num_vowels = 0 # Her kelimenin sesli harf sayısını tutmak için bir sayaç

        # Her harfi kontrol et ve sesli harfse sayacı artır
        for letter in word:
            if letter in vowels:
                num_vowels += 1

        # Sayaç çift sayıda is kelimenin puanını 2 artır, değilse 1 artır
        if num_vowels % 2 == 0:
            score += 2
        else:
            score += 1
        
    return score

# Girdi al ve kelimeleri ayırarak score_words fonksiyonunu çağır
n = int(input())
words = input().split()
print(score_words(words))