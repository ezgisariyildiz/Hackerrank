import re
# Bir regex deseni kullanarak e-posta adreslerinin doğruluğunu kontrol ediyoruz
def fun(s):
    pattern = re.compile(r'^[a-zA-Z0-9_-] + @[a-zA-Z0-9] + \.[a-zA-Z]{1,3}$')
    return pattern.match(s)

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)

'''
^ : Satirin baslangici
[a-zA-Z0-9_-]+ : Kullanici adi kismi, harfler, rakamlar, tire ve alt çizgi içerebilir ve en az bir karakterden oluşmalidir.
@ : E-posta adreslerindeki ayirici
[a-zA-Z0-9]+ : Alan adi kismi, harfler ve rakamlar içerebilir.
\. : Domainin ve uzantinin ayriricisi
[a-zA-Z]{1,3} : Domain uzantisi, en az bir ve en fazla üç harften oluşmalidirr.
$ : Satirin sonu
'''