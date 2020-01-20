import requests
import pprint
from bs4 import BeautifulSoup
import json


pp = pprint.PrettyPrinter(indent=4)


with open('eng.txt') as f:
    lines = [line.rstrip() for line in f]

def craw_tureng(arg):
    rows = []

    if isinstance(arg, str):
        url = "https://tureng.com/tr/turkce-ingilizce/" + arg
        print(url)
    else:
        print("arguman hatalı geldi")
        exit(1)

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    tltn_table = soup.find_all('table', limit=2)

    try:
        t1 = tltn_table.pop()  # ilk tablo direk çeviri
        t1_rows = t1.find_all('tr')
        row_list = list()

        for tr in t1_rows:
            td = tr.find_all('td')
            row = [i.text for i in td]
            if len(td) == 5:
                row_list.append(row)
        # pp.pprint(row_list)

        with open(arg+'.json', 'w', encoding='utf-8') as f:
            json.dump(row_list, f, ensure_ascii=False, indent=4)

    except Exception as e:
        print(e)


index = 0
for i in lines:
    print(index)
    craw_tureng(i)
    index += 1
    if i == 3:
        break
