import xml.etree.ElementTree as ET
import requests
def create_xml(name,text):
    root = ET.Element("root")
    child = ET.SubElement(root, "data")
    child.text = text
    tree = ET.ElementTree(root)
    xml_file = tree.write(f'{name}.xml')
    return 'data.xml'


# DB 서버 경로
DB_URL= 'http://54.180.116.44:8000'



# try:
#     response= requests.get(r"http://59.14.135.171:21330/url/DB/")
#     DB_URL= response.text
# except:
#     print("error")


def getDB_URL(element):
    return f"{DB_URL}/api/{element}/"

