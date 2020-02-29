import requests
import lxml.html as lh
import csv

urls = []
url_martie = "https://en.tutiempo.net/climate/03-2017/ws-153460.html"
url_aprilie = "https://en.tutiempo.net/climate/04-2017/ws-153460.html"
url_mai = "https://en.tutiempo.net/climate/05-2017/ws-153460.html"
url_iunie = "https://en.tutiempo.net/climate/06-2017/ws-153460.html"
url_iulie = "https://en.tutiempo.net/climate/07-2017/ws-153460.html"
url_august = "https://en.tutiempo.net/climate/08-2017/ws-153460.html"

urls.append(url_martie)
urls.append(url_aprilie)
urls.append(url_mai)
urls.append(url_iunie)
urls.append(url_iulie)
urls.append(url_august)

columns_for_write =[]
for i in range(33):
    l = ['', '', '', '', '', '']
    columns_for_write.append(l)

print(len(columns_for_write))

i = 0
for month in urls:
    page = requests.get(month)
    doc = lh.fromstring(page.content)
    table_elements = doc.xpath('//table')
    tr_elements = table_elements[3].xpath('//tr')
    rows = [r for r in tr_elements if len(r) == 15]
    j = 0
    for r in rows:
        col = r[6].text_content()
        columns_for_write[j][i]=col
        j += 1
    i += 1

for i in columns_for_write:
    print(len(i))

print(columns_for_write)

with open('alunu.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Martie', 'Aprilie', 'Mai', 'Iunie', 'Iulie', 'August'])
    for r in columns_for_write:
        writer.writerow(r)


