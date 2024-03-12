import queue as Queue

cntr = 0

class Node:
    def __init__(self, freq, data):
        self.freq = freq  # Karakterin frekansı
        self.data = data  # Karakter verisi
        self.left = None  # Left child node u
        self.right = None  # Right child nod eu
        global cntr
        self._count = cntr  # Node sayacı (sıralama için kullanılır)
        cntr = cntr + 1
        
    def __lt__(self, other):
        if self.freq != other.freq:
            return self.freq < other.freq
        return self._count < other._count

# Huffman ağacını oluşturan ve kök node döndüren fonksiyon
def huffman_hidden():
    q = Queue.PriorityQueue()

    # Karakter frekanslarına göre öncelik kuyruğuna nodeları ekle
    for key in freq:
        q.put((freq[key], key, Node(freq[key], key) ))
    
    # Öncelik kuyruğundan nodeları alarak Huffman ağacını oluştur
    while q.qsize() != 1:
        a = q.get()
        b = q.get()
        obj = Node(a[0] + b[0], '\0' )  # Yeni bir node oluştur ve frekansları topla
        obj.left = a[2]  # Left child node u ata
        obj.right = b[2]  # Right child node u ata
        q.put((obj.freq, obj.data, obj ))  # Yeni node u öncelik kuyruğuna ekle
        
    root = q.get()  # Kök node u al
    root = root[2]  # Kök node objesini al
    return root  # Kök node u döndür

# Huffman ağacını dolaşarak her karakterin kodunu oluşturan yardımcı fonksiyon
def dfs_hidden(obj, already):
    if(obj == None):
        return
    elif(obj.data != '\0'):
        code_hidden[obj.data] = already
        
    dfs_hidden(obj.right, already + "1")  # Right child ı ziyaret et (1 ekleyerek)
    dfs_hidden(obj.left, already + "0")  # Left child ı ziyaret et (0 ekleyerek)

# Huffman kodunu çözen fonksiyon
def decodeHuff(root, s):
    decoded_string = ""
    current = root
    for bit in s:
        if bit == '0':
            current = current.left  # LEft child a git
        else:
            current = current.right  # Right child a git
        if current.left is None and current.right is None:
            decoded_string += current.data  # Yaprak node a ulaşıldı, karakteri ekle
            current = root  # Node a geri dön
    print(decoded_string)  # Çözülmüş diziyi yazdır

ip = input()
freq = {}  # Her karakterin frekansını tutan bir sözlük

cntr = 0

# Girdi içindeki her bir karakterin frekansını hesapla
for ch in ip:
    if(freq.get(ch) == None):
        freq[ch] = 1
    else:
        freq[ch]+=1

root = huffman_hidden()  # Huffman ağacının kökünü oluştur

code_hidden = {}  # Her karakterin kodunu tutan bir sözlük

dfs_hidden(root, "")  # Huffman ağacını dolaşarak her karakterin kodunu oluştur

# Girişteki karakter sayısı 1 ise, bu karakterin kodunu "0" olarak ayarla
if len(code_hidden) == 1:
    for key in code_hidden:
        code_hidden[key] = "0"

toBeDecoded = ""

# Giriş dizisi için Huffman kodlamasını uygula
for ch in ip:
   toBeDecoded += code_hidden[ch]

decodeHuff(root, toBeDecoded)  # Huffman kodunu çöz
