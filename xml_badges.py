import xml.etree.ElementTree as ET
badgedic= {}
tree=ET.parse('Badges.xml')
root=tree.getroot()
for row in root:
    user= row.get('UserId')
    badge=row.get('Name')
    if user not in badgedic():
        badgedic[user]=[badge]
    else:
        badgedic[user].append(badge)

    
    

