#-------------------------------------------------------------------------------
# Name:        BuildfElo1
# Purpose:
#
# Author:      vyz
#
# Created:     20.03.2019
# Modified:    17.04.2019
#-------------------------------------------------------------------------------
import xml.etree.ElementTree as ET
from Classo import Opera as ClOp
from Classo import fElo as Fel

filo = "E:\\Wabo\\Scamo\\Pyatnyshky\\Ksamalo\\OperaClassoWithIerro.xml"
fout = "E:\\Wabo\\Scamo\\Pyatnyshky\\Ksamalo\\fElosy.xml"
eliky = {}

def main():
    opels = ClOp.GetDictionaryOperationsFromXmlFile(filo=filo)
    ll = ('TAbstractOperationEntity', 'TOperationPublicDescription', 'TOperationDescriptor', 'TAbstractTechnologicalOperation', 'TSTAbstractMillOp', 'TSTMillOp', 'TSTAbstract5DOp', 'RoughingRotaryMachiningOp')
    dira = 'D:\\Progo\\sTwelo\\Supplement\\Operations\\'
    fely = MinoFromList(ll, opels, dira)
    Fel.XmlWriteFeloClasso(fout, fely)

def MinoFromList(ll, opels, dira) :
    for kopa in ll :
        fila = opels[kopa].filo
        tree = ET.ElementTree(file=dira+fila)
        root = tree.getroot()
        for child in root:
            if child.tag == "SCType" and child.attrib.get('ID') == kopa :
                for zz in child:
                    if zz.tag == "SCType" :
                        RecursoSCType(zz, opels[kopa], 0, '')
    return eliky

def RecursoSCType(elem, opera, levelo, fazer) :
    """
    elem -- xml-элемент типа SCType
    opera --  операция, в которой нашли данный элемент
    levelo -- уровень вложенности, контролируемый максимум 10
    fazer -- ID SCType-элемента, в который вложен текущий
    """
    if levelo > 10 :
        assert("levelo in RecursoSCType >>> 10")
    vnsushy = {}
    vndefy = {}
    for vn in elem:
        if vn.tag == "SCType":
            RecursoSCType(vn, opera, levelo+1, elem.attrib.get('ID'))
        else :
            vnsushy[vn.tag] = len(vn)
    elik = Fel.fElo(opera, elem.attrib, vnsushy, vndefy, levelo, fazer)
    eliky[elik.kia] = elik
    print("opera - %s  levelo - %i fazer - %s el - %s leno - %i" % (opera.kia, levelo, fazer, elik.kia, len(eliky)))


def XmlFelosyWrite(flo, els) :
    start = None
    for elo in els.values() :
        if elo.ierro == 'A':
            start = elo
            break;
    root = ET.Element(start.kia)
    EloTree(els, elo, root)
    tree = ET.ElementTree(root)
    with open(flo, "bw") as fh:
        tree.write(fh, encoding = "utf-8", xml_declaration=True, method="xml")

def EloTree(alls, starto, elo) :
    elo.set('typo', starto.typo)
    elo.set('filo', starto.filo)
    elo.set('regtypo', starto.regtypo)
    elo.set('guido', starto.guido)

    newa = []
    for opo in alls.values():
        tapo = opo.typo
        if tapo == starto.kia :
            newa.append(opo)
    for nelo in newa :
        etel = ET.Element(nelo.kia)
        EloTree(alls, nelo, etel)
        elo.append(etel)

if __name__ == '__main__':
    main()
