import requests
import xml.etree.ElementTree as ET

items = set()
nums = range(1, 47)

for num in nums:
    print(str(num))
    r = requests.get("http://radiko.jp/v3/station/list/JP" + str(num) + ".xml")
    root = ET.fromstring(r.text)
    for child in root:
    
        url = "http://radiko.jp/v3/program/station/weekly/" + child.find('id').text + ".xml"
        print("" + url)
        rprog = requests.get(url)
        rprog.encoding = rprog.apparent_encoding
        for prog in ET.fromstring(rprog.text).iter('prog'):
            site = prog.find('url').text
            if site is not None:
                items.add(site)

with open('out.txt', mode='w') as f:
    for item in items:
        f.write(item)
        f.write('\n')