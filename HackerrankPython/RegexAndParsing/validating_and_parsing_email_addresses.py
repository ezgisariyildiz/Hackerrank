import email.utils

def is_valid_email(email):
    # email.utils.parseaddr() işlevi, verilen e-posta adresini ayrıştırır ve (ad, adres) şeklinde bir tuple döndürür. 
    # Bu satırda, verilen e-posta adresi ayrıştırılır ve parsed_email değişkenine atanır
    parsed_email = email.utils.parseaddr(email)
    # '@' işareti bulunup bulunmadığı kontrol edilir
    return '@' in parsed_email[1]

if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        # Kullanıcıdan alınan giriş iki parçaya bölünür, İlk parça name değişkenine, ikinci parça ise email değişkenine atanır
        name, email = input().split()
        if is_valid_email(email):
            print(f"{name} <{email}>")