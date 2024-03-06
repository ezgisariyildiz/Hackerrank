from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    # Herhangi bir yorum bulunduğunda çağrılır
    def handle_comment(self, data):
        if '\n' in data:
            # eğer çok satırlı bir yorum ise
            print(">>> Multi-line Comment")
        else:
            # eğer tek satırlı bir yorum ise
            print(">>> Single-line Comment")
        print(data)

    # gelen veriyi alır ve eğer veri boşluklar hariç herhangi bir karakter içeriyorsa
    def handle_data(self, data):
        if data.strip():
            # yazdırır
            print(">>> Data")
            print(data)

if __name__ == '__main__':
    parser = MyHTMLParser()
    n = int(input())
    # Kullanıcıdan satır satır HTML kodunu alıyoruz ve bu kodları bir dize listesi olarak birleştirerek tek bir dize haline getiriyoruz
    html_code = "\n".join([input() for _ in range(n)])
    parser.feed(html_code)