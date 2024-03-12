class Node:
    def __init__(self, info): 
        self.info = info  # Node un değeri
        self.left = None  # LEft child node u
        self.right = None  # Right child node u
        self.level = None  # Node un seviyesi

    def __str__(self):
        return str(self.info)  # Node değerini döndür

class BinarySearchTree:
    def __init__(self): 
        self.root = None  # Kök node tanımla

    def create(self, val):  
        if self.root == None:  # Eğer ağaç boşsa
            self.root = Node(val)  # Kök node oluştur
        else:
            current = self.root  # Ağacın kökünden başla
         
            while True:
                if val < current.info:  # Eğer eklenecek değer mevcut düğümün değerinden küçükse
                    if current.left:  # Eğer mevcut düğümün left child varsa
                        current = current.left  # Mevcut düğümü right child a kaydır
                    else:
                        current.left = Node(val)  # Left child a yeni bir düğüm ekle
                        break
                elif val > current.info:  # Eğer eklenecek değer mevcut düğümün değerinden büyükse
                    if current.right:  # Eğer mevcut düğümün right child varsa
                        current = current.right  # Mevcut düğümü right child a kaydır
                    else:
                        current.right = Node(val)  # Right child a yeni bir düğüm ekle
                        break
                else:
                    break  # Eğer eklenecek değer zaten ağaçta varsa döngüyü sonlandır

"""
Node şu şekilde tanımlanır:
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""

def preOrder(root):
    if root:
        print(root.info, end=" ")  # Mevcut düğümün değerini yazdır
        preOrder(root.left)  # Left child a git
        preOrder(root.right)  # right child a git

# Örnek kullanım:
tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

preOrder(tree.root)


