import requests as rq
import xml.etree.ElementTree as ET

t = 'out.txt'
f = open(t)
line = f.readline()
for i in range(3):
    line = f.readline()

print(line[:-1])
r = rq.get(line[:-1])
r.encoding = r.apparent_encoding
print(r.text)

f.close