import requests
import lxml
from bs4 import BeautifulSoup
import pprint

# https://tureng.com/tr/turkce-ingilizce

# TODO 
# url stringine ekleyerek yapabilirim 
# bir yerden sonra click'e geçebilirim

# kelimenin diline göre ingilizce türkçe sırası degişiyor 
# tr-eng mi eng tr mi anlamaya gerek varmı 

def main():
    pp = pprint.PrettyPrinter(indent=4)

    r = requests.get("https://tureng.com/tr/turkce-ingilizce/deneme")

    # post = requests.post("https://tureng.com/tr/turkce-ingilizce")

    soup = BeautifulSoup(r.text , 'lxml')

    # önce çeviri tablosunu bul  
    # direkt find metodu kullanılabilir yada limit kullanılabilir 
    tltn_table = soup.find_all('table', limit=2) 

    t2 = tltn_table.pop() # ikinci tablo diger kelimeler ile 
    t1 = tltn_table.pop() # ilk tablo direk çeviri

    t1_rows = t1.find_all('tr')
    row_list = list()

    for tr in t1_rows:
        td = tr.find_all('td')
        row = [i.text for i in td]
        if len(td) == 5:
            row_list.append(row)
        
    #print(row_list)
    pp.pprint(row_list)

if __name__ == '__main__':
    main()

