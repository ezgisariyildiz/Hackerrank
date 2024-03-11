class TextEditor:
    def __init__(self):
        # TextEditör sınıfının yapıcı metodunda, metin ve bir geçmiş listesi oluşturuluyor.
        self.text = ""  # Metin boş olarak başlatılıyor.
        self.history = []  # İşlem geçmişi boş olarak başlatılıyor.

    def append(self, word):
        # Metin sonuna kelime eklemek için kullanılan metod.
        # Önceki metni geçmişe ekleyip, sonra yeni kelimeyi metnin sonuna ekliyor.
        self.history.append(self.text)
        self.text += word

    def erase(self, k):
        # Metinden son k karakteri silmek için kullanılan metod.
        # Önceki metni geçmişe ekleyip, sonra metnin sonundan k kadar karakteri siliyor.
        self.history.append(self.text)
        self.text = self.text[:-k]

    def get(self, k):
        # Belirli bir karakteri almak için kullanılan metod.
        # Verilen dizindeki karakteri yazdırıyor.
        print(self.text[k-1])

    def undo(self):
        # Son yapılan işlemi geri almak için kullanılan metod.
        # Geçmişte bir işlem varsa, en son işlemi geri alıyor.
        if self.history:
            self.text = self.history.pop()

def main():
    n = int(input().strip())  # İşlem sayısını alıyoruz.
    editor = TextEditor()  # TextEditor sınıfından bir örnek oluşturuyoruz.

    for _ in range(n):
        operation = input().strip().split()  # İşlemi alıyoruz ve boşluklara göre ayırıyoruz.
        op_type = int(operation[0])  # İşlem türünü belirliyoruz.

        if op_type == 1:
            # Eğer işlem türü 1 ise, append metodunu çağırarak kelimeyi metnin sonuna ekliyoruz.
            editor.append(operation[1])
        elif op_type == 2:
            # Eğer işlem türü 2 ise, erase metodunu çağırarak metinden belirli sayıda karakteri siliyoruz.
            editor.erase(int(operation[1]))
        elif op_type == 3:
            # Eğer işlem türü 3 ise, get metodunu çağırarak belirli bir karakteri alıp yazdırıyoruz.
            editor.get(int(operation[1]))
        elif op_type == 4:
            # Eğer işlem türü 4 ise, undo metodunu çağırarak son işlemi geri alıyoruz.
            editor.undo()

if __name__ == "__main__":
    main()
