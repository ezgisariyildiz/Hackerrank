def print_rangoli(size):
    w = (size - 1) * 2 + ((size * 2) - 1)
    
    # Upper half
    for i in range(1, size):
        number_of_letter = (i * 2) - 1
        s = ""
        letter_value = 97 + size - 1
        for i in range(number_of_letter):
            if i != 0:
                s += "-"
            s += chr(letter_value)
            if i < (number_of_letter - 1) / 2:
                letter_value = letter_value - 1
            else:
                letter_value = letter_value + 1
        print(s.center(w, "-"))

    # Bottom half
    for i in range(size, 0, -1):
        number_of_letter = (i * 2) - 1
        s = ""
        letter_value = 97 + size - 1
        for i in range(number_of_letter):
            if i != 0:
                s += "-"
            s += chr(letter_value)
            if i < (number_of_letter - 1) / 2:
                letter_value = letter_value - 1
            else:
                letter_value = letter_value + 1
        print(s.center(w, "-"))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)