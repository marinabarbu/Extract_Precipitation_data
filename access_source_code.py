import requests
import lxml.html as lh

url = "https://en.tutiempo.net/climate/05-2017/ws-153460.html"
page = requests.get(url)
#print(len(page.text))
#print(len(np(page.text.split())))
doc = lh.fromstring(page.content)
table_elements = doc.xpath('//table')
#print([len(T) for T in table_elements[:30]])
tr_elements = table_elements[3].xpath('//tr')
#print([len(T) for T in tr_elements])
rows = [r for r in tr_elements if len(r) == 15]

'''
for r in rows:
    for i in range(len(r)):
        if i == 6:
            col = r[i].text_content()
            print(col)
'''

for r in rows:
    col = r[6].text_content()
    print(col)



