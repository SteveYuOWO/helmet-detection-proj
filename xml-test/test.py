import xml.etree.ElementTree as ET

tree = ET.parse('data.xml')

# 获取根节点
root = tree.getroot()
print("root tag: %s" % root.tag)
print("root attrbute: %s" % root.attrib)

for child in root:
    print(child.tag, child.attrib)

# 取root的0标签中的1标签中的text
print(root[0][1].text)


for country in root.findall('country'):
     rank = int(country.find('rank').text)
     if rank > 50:
         root.remove(country)
tree.write('/Users/steveyu/PycharmProjects/helmet-detection-proj/xml-test/output.xml')

ele = root.find('country')
print(ele.attrib['name'])