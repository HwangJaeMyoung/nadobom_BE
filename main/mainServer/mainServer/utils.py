import xml.etree.ElementTree as ET

def create_xml(name,text):
    root = ET.Element("root")
    child = ET.SubElement(root, "data")
    child.text = text
    tree = ET.ElementTree(root)
    xml_file = tree.write(f'{name}.xml')
    return 'data.xml'


# DB 서버 경로
DB_URL= 'http://127.0.0.1:8000/'


def getDB_URL(element):
    return f"{DB_URL}/api/{element}/"

