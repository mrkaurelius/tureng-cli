import requests
import pprint
from bs4 import BeautifulSoup


pp = pprint.PrettyPrinter(indent=4)


def get_tureng(arg):
    if isinstance(arg, str):
        url = "https://tureng.com/tr/turkce-ingilizce/" + arg
        print(url)
    else:
        print("arguman hatalı geldi")
        exit(1)

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    all_tables = soup.find_all('table')

    # print(len(all_tables)) # eleman sayisini dondurur
    # gelen cevabı arama, belli bir sıraya gore sonucları gosterme
 
    for table in all_tables: # iterasyon nasıl daha efektif olur ?
        rows = table.find_all('tr')
        for row in rows:
            cells = row.find_all('td')
            if len(cells) == 5:
                # row_list.append(row)
                print(cells[1].text.strip(), cells[2].text.strip(), cells[3].text)


    # pp.pprint(row_list)


# get_tureng("deneme")
