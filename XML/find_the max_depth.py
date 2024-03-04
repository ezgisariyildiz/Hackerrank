import xml.etree.ElementTree as etree

# # En derin iç içe geçme seviyesini saklamak için bir değişken tanımlanır.
maxdepth = 0

def depth(elem, level):
    global maxdepth # global key ile maxdepth i global kapsamda tanımlıyoruz

    if level == maxdepth: # Eğer geçerli seviye en derin seviye ise
        maxdepth += 1 # ... en derin seviyeyi bir artır

    for child in elem: # Her bir alt elemanı döngüye alarak
        depth(child, level + 1) #... ve onların derinliğini hesaplamak için fonksiyonu yeniden çağırırız
    
if __name__ == '__main__':
    n = int(input()) # XML belgesinin satır sayısını alırız
    xml = "" # XML belgesini saklamak için dize bir oluşturduk
    for i in range(n): # Her bir satırı almak için döngü başlattık
        xml = xml + input() + "\n" # Her satırı XML dizesine ekleriz ve bir sonraki satıra geçeriz

    tree = etree.ElementTree(etree.fromstring(xml)) # ElementTree nesnesi oluşturduk ve XML dizesini analiz ettik
    depth(tree.getroot(), -1) # Kök node un derinliğini hesaplamak için depth fonksiyonunu çağırdık
    print(maxdepth) # En derin içi içe geçme seviyesi yazdırılır

'''
İç içe geçme seviyesi, bir yapi içindeki alt yapilarin ne kadar derin olduğunu belirtir.
Örneğin, bir XML belgesinde iç içe geçen etiketler varsa, her bir iç içe geçen etiketin seviyesi, kök etiketten ne kadar derin olduğunu belirtir.
'''