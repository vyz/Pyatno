#-------------------------------------------------------------------------------
# Name:        fElo Class
# Purpose:
#
# Author:      vyz
#
# Created:     19.03.2019
# Modified:    27.03.2019
#-------------------------------------------------------------------------------

import xml.etree.ElementTree as ET
#import Opera as ClOp

class fElo:

    def __init__(self, papa, attro, vnsushy, vndefy, levo = 0, ifa = ''):
        self.kia = attro['ID']                                                #1
        """Не имеет права быть пустым."""
        self.typo = attro['type'] if 'type' in attro else (attro['Type'] if 'Type' in attro else'z_pusto')           #2
        self.capta = attro['Caption'] if 'Caption' in attro else 'z_pusto'    #3
        self.kata = attro['Category'] if 'Category' in attro else 'z_pusto'   #4
        self.bCompact = attro['Compact'] if 'Compact' in attro else 'z_pusto'   #5 Булево значение
        self.defo = attro['DefaultValue'] if 'DefaultValue' in attro else (attro['DefalutValue'] if 'DefalutValue' in attro else'z_pusto')   #6
        self.bEnabled = attro['Enabled'] if 'Enabled' in attro else 'z_pusto'   #7 Булево значение
        self.bExpanded = attro['Expanded'] if 'Expanded' in attro else 'z_pusto'   #8 Булево значение
        self.imago = attro['ImageFile'] if 'ImageFile' in attro else 'z_pusto'   #9
        self.dimokind = attro['DimensionKind'] if 'DimensionKind' in attro else 'z_pusto'   #10
        self.bIsdDinamo = attro['IsDynamic'] if 'IsDynamic' in attro else 'z_pusto'   #11 Булево значение
        self.bIsJoboProp = attro['IsJobProp'] if 'IsJobProp' in attro else 'z_pusto'   #12 Булево значение
        self.parento = attro['Parent'] if 'Parent' in attro else 'z_pusto'   #13
        self.presenter = attro['PresenterVO'] if 'PresenterVO' in attro else 'z_pusto'   #14
        self.prio = attro['Priority'] if 'Priority' in attro else 'z_pusto'   #15
        self.breadonly = attro['ReadOnly'] if 'ReadOnly' in attro else 'z_pusto'   #16 Булево значение
        self.reseto = attro['ResetMode'] if 'ResetMode' in attro else 'z_pusto'   #17
        self.transo = attro['Transparent'] if 'Transparent' in attro else 'z_pusto'   #18
        self.edizmo = attro['UnitsChar'] if 'UnitsChar' in attro else 'z_pusto'   #19
        self.versus = attro['Version'] if 'Version' in attro else 'z_pusto'   #20
        self.visiblo = attro['Visible'] if 'Visible' in attro else (attro['visible'] if 'visible' in attro else'z_pusto')   #21
        #Заход для новых атрибутов у элементов 1-го уровня вложенности 16.04.2019
        self.enabledvalo = attro['EnabledValue'] if 'EnabledValue' in attro else 'z_pusto'   #22
        self.inchoDefo = attro['InchDefaultValue'] if 'InchDefaultValue' in attro else 'z_pusto'   #23
        self.bIsInErrorState = attro['IsInErrorState'] if 'IsInErrorState' in attro else 'z_pusto'   #24 Булево значение, но в виде выражения
        self.bIsRadioEdit = attro['IsRadioEdit'] if 'IsRadioEdit' in attro else 'z_pusto'   #25 Булево значение
        self.bObsolete = attro['Obsolete'] if 'Obsolete' in attro else 'z_pusto'   #26 Булево значение
        self.texto = attro['Text'] if 'Text' in attro else 'z_pusto'   #27 Булево значение
        self.charleno = attro['MaxCharsCount'] if 'MaxCharsCount' in attro else 'z_pusto'   #28


        self.Opera = papa
        """Операция, в которой определена сущность"""
        self.levlo = levo
        """Уровень вложенности сущности. Непосредственно определённые в элементе операции = 0"""
        self.iFa = ifa
        """ID сущности в которую вложена данная"""
        self.Dopo = {}
        for k, v in sorted(attro.items()):
            if not k in ('ID', 'type', 'Type', 'Caption', 'Category', 'Compact', 'DefaultValue', 'DefalutValue', 'Enabled',
                         'Expanded', 'ImageFile', 'DimensionKind', 'IsDynamic', 'IsJobProp', 'Parent', 'PresenterVO', 'Priority',
                         'ReadOnly', 'ResetMode', 'Transparent', 'UnitsChar', 'Version', 'Visible', 'visible',
                         'EnabledValue', 'InchDefaultValue', 'IsInErrorState', 'IsRadioEdit', 'Obsolete', 'Text', 'MaxCharsCount' ) :
                self.Dopo[k] = v
        self.sushy = vnsushy
        self.defy = vndefy

    def ToXml(self):
        elko = ET.Element('fElo')
        elko.set('kia', self.kia)
        elko.set('typo', self.typo)
        elko.set('capta', self.capta)
        elko.set('kata', self.kata)
        elko.set('defo', self.defo)
        elko.set('imago', self.imago)
        elko.set('bEnabled', self.bEnabled)
        elko.set('bCompact', self.bCompact)
        elko.set('bExpanded', self.bExpanded)
        elko.set('dimokind', self.dimokind)
        elko.set('bIsdDinamo', self.bIsdDinamo)
        elko.set('bIsJoboProp', self.bIsJoboProp)
        elko.set('parento', self.parento)
        elko.set('presenter', self.presenter)
        elko.set('prio', self.prio)
        elko.set('breadonly', self.breadonly)
        elko.set('reseto', self.reseto)
        elko.set('transo', self.transo)
        elko.set('edizmo', self.edizmo)
        elko.set('versus', self.versus)
        elko.set('visiblo', self.visiblo)
        elko.set('enabledvalo', self.enabledvalo)
        elko.set('inchoDefo', self.inchoDefo)
        elko.set('bIsInErrorState', self.bIsInErrorState)
        elko.set('bIsRadioEdit', self.bIsRadioEdit)
        elko.set('bObsolete', self.bObsolete)
        elko.set('texto', self.texto)
        elko.set('charleno', self.charleno)

        elko.set('Opera', self.Opera.ierro + ' ' + self.Opera.kia)
        elko.set('Level', str(self.levlo))
        elko.set('IFather', self.iFa)

        stroka = ''
        for k, v in self.Dopo.items():
            stroka += "{} : {} ".format(k, v)
        elko.set('Dopo', stroka)
        stroka = ''
        for k, v in self.sushy.items():
            stroka += "{} : {} ".format(k, v)
        elko.set('DopSu', stroka)
        stroka = ''
        for k, v in self.defy.items():
            stroka += "{} : {} ".format(k, v)
        elko.set('DopDf', stroka)
        return elko

#Ещё не трогалось
def GetDictionaryFelosFromXmlFile(filo = "E:\\Wabo\\Scamo\\Pyatnyshky\\Ksamalo\\fElosy.xml") :
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

def XmlWriteFeloClasso(flo, elems):
    root = ET.Element("fElosy")
    for k, v in sorted(elems.items()):
        root.append(v.ToXml())
    tree = ET.ElementTree(root)
    with open(flo, "wb") as fh:
        tree.write(fh, encoding = "utf-8", xml_declaration=True, method="xml")
