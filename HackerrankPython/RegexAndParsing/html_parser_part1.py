from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    # Başlangıç etiketinin adını yazdır ve ardından her bir niteliğin adını ve değerini yazdır
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for attr in attrs:
            print(f"-> {attr[0]} > {attr[1]}")
            
    # Bitiş etiketlerini işlemek için kullan
    def handle_endtag(self,tag):
        print("End   :", tag)

    # Boş etiketleri işlemek için kullanılır
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for attr in attrs:
            print(f"-> {attr[0]} > {attr[1]}")

if __name__ == '__main__':
    n = int(input())
    parser = MyHTMLParser()
    for _ in range(n):
        parser.feed(input())
