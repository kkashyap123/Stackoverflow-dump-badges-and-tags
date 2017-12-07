import xml.etree.ElementTree as ET
tagdic= {}
tree=ET.parse('tags.xml')
root=tree.getroot()
for row in root.findall('row'):
    name= row.get('TagName')
    tagdic[name]= row.attrib
print(tagdic)