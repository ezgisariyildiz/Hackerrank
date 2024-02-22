if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1): 
        print(i,end="")

########## ikinci yol ###########

def print_numbers(n):
    result = ""
    for i in range(1, n + 1):
        result += str(i)
    print(result)

# STDIN'den girdiyi oku
n = int(input().strip())

# Fonksiyonu çağır ve sonucu yazdır
print_numbers(n)
