import re

def is_valid_mobile_number(s):
    regex = r'[789]\d{9}$'
    return bool(re.match(regex, s))

n = int(input().strip())
inputs = [input().strip() for _ in range(n)]

for number in inputs:
    if is_valid_mobile_number(number):
        print("YES")
    else:
        print("NO")