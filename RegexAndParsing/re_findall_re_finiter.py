import re

def find_vowel_substrings(s):
    pattern = r'(?<=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])[aeiouAEIOU]{2,}(?=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])'
    
    substrings = re.findall(pattern, s)

    if substrings:
        for substring in substrings:
            print(substring)
        else:
            print(-1)

if __name__ == '__main__':
    s = input()
    find_vowel_substrings(s)