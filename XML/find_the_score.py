import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    # Bu işlev bir XML node unun içindeki özniteliklerin sayısını hesaplar
    # node: XML node u
    # return: Node daki özniteliklerin toplamı
    return sum(len(elem.attrib) for elem in node.iter())

if __name__ == '__main__':
    # Standart girişten bir sayı okunur ve atlanır
    sys.stdin.readline()

    # Girişten gelen XML belgesi okunur
    xml = sys.stdin.read()

    # XML belgesi ElementTree tree yapısına dönüştürülür
    tree = etree.ElementTree(etree.fromstring(xml))

    # Tree yapısının kök node u alınır
    root = tree.getroot()

    # Kök node daki attributelerin sayısı hesaplanır ve yazdırılır
    print(get_attr_number(root))