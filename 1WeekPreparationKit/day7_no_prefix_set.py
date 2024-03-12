#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'noPrefix' function below.
#
# The function accepts STRING_ARRAY words as parameter.

def noPrefix(words):
    encoder = dict()  # Boş bir sözlük oluşturulur, bu sözlük kelime öbeklerini kodlamak için kullanılacak
    for s in words:  # Kelimelerin her biri üzerinde döngü
        tempdict = encoder  # Geçici bir sözlük oluşturulur, her kelimeyi kodlamak için kullanılacak
        for i, l in enumerate(s):  # Her bir kelimenin karakterleri üzerinde döngü
            if l in tempdict.keys():  # Karakter, geçici sözlükte bir anahtar olarak var mı kontrol edilir
                tempdict = tempdict.get(l)  # Eğer varsa, geçici sözlük bu anahtarın değerini alır
                if tempdict is True or i == len(s) - 1:  # Eğer değer True ise veya kelimenin sonuna gelindiyse
                    print(f'BAD SET\n{s}')  # "BAD SET" yazdırılır ve kelime ekrana basılır
                    return  # Fonksiyon sonlandırılır
            else:  # Eğer karakter, geçici sözlükte bir anahtar olarak yoksa
                if i == len(s) - 1:  # Eğer bu karakter kelimenin son karakteriyse
                    tempdict[l] = True  # Geçici sözlüğe bu karakteri True olarak ekler (kelimenin tamamını kodladığını belirtir)
                else:  # Eğer bu karakter kelimenin son karakteri değilse
                    tempdict[l] = dict()  # Geçici sözlüğe bu karakter için bir alt sözlük oluşturulur
                    tempdict = tempdict[l]  # Alt sözlüğe geçiş yapılır
    print('GOOD SET')  # Eğer herhangi bir kelime bir başka kelimenin ön eki değilse, "GOOD SET" yazdırılır

if __name__ == '__main__':
    n = int(input().strip())  # Kelime sayısı alınır

    words = []  # Kelimelerin depolanacağı bir liste oluşturulur

    for _ in range(n):  # Kelimeler alınır ve listeye eklenir
        words_item = input()
        words.append(words_item)

    noPrefix(words)  # Fonksiyon çağrılır ve sonuç yazdırılır
