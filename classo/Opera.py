#-------------------------------------------------------------------------------
# Name:        Opera Class
# Purpose:
#
# Author:      vyz
#
# Created:     07.02.2019
# Modified:    26.02.2019
#-------------------------------------------------------------------------------

import xml.etree.ElementTree as ET

class Opera:

    def __init__(self, dicto):
        self.kia = dicto['kia']                  #1
        """Не имеет права быть пустым."""
        self.guido = dicto['guido']              #2
        self.filo = dicto['filo']                #3
        self.typo = dicto['typo']                #4
        self.grupo = dicto['grupo']              #5
        self.capta = dicto['capta']              #6
        self.commento = dicto['commento']        #7
        self.regtypo = dicto['regtypo']          #8
        #Не инициализируемые в параметрах поля
        self.ierro = 'z_pusto'

    def ToXml(self):
        elko = ET.Element('Opera')
        elko.set('kia', self.kia)
        elko.set('guido', self.guido)
        elko.set('filo', self.filo)
        elko.set('typo', self.typo)
        elko.set('grupo', self.grupo)
        elko.set('capta', self.capta)
        elko.set('commento', self.commento)
        elko.set('regtypo', self.regtypo)
        #Дополнительные поля"
        elko.set('ierro', self.ierro)
        return elko

def GetDictionaryOperationsFromXmlFile(filo = "E:\\Wabo\\Scamo\\Pyatnyshky\\Ksamalo\\OperaClasso.xml") :
    tree = ET.ElementTree(file=filo)
    root = tree.getroot()
    els = {}
    for child in root:
        if child.tag == "Opera":
            dicto = {}
            dicto['kia'] = child.attrib.get('kia')
            dicto['guido'] = child.attrib.get('guido')
            dicto['filo'] = child.attrib.get('filo')
            dicto['typo'] = child.attrib.get('typo')
            dicto['grupo'] = child.attrib.get('grupo')
            dicto['capta'] = child.attrib.get('capta')
            dicto['commento'] = child.attrib.get('commento')
            dicto['regtypo'] = child.attrib.get('regtypo')
            els[dicto['kia']] = Opera(dicto)
            aierro = child.attrib.get('ierro')
            els[dicto['kia']].ierro = aierro
    return els

def XmlWriteOperaClasso(flo, elems):
    root = ET.Element("OperaClassoAbso")
    for k, v in sorted(elems.items()):
        root.append(v.ToXml())
    tree = ET.ElementTree(root)
    with open(flo, "wb") as fh:
        tree.write(fh, encoding = "utf-8", xml_declaration=True, method="xml")
