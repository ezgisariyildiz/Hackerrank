def wrapper(f):
    def fun(l):
        # Cep telefonu numarasını standart formata dönüştür
        def standardize_phone_number(phone):
            return "+91" + phone[-10:-5] + " " + phone[-5:]
        
        # Cep telefonu numaralarını sırala ve standart formata dönüştürerek yazdır
        f(sorted(map(standardize_phone_number, l)))
    
    return fun

@wrapper
def sort_phone(l):
    print(*l, sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)        