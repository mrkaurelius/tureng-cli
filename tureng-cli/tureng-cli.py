from bs4 import BeautifulSoup
from fzf_process import choose_word
from tureng_web import get_tureng
import click
import time


# veri tabanı ekle
#   gelen sozcuk veri tabanında varsa internette arama


def main():
    word = choose_word()

    word = word.strip()

    print("get_tureng calisiyor", word)
    get_tureng(word)


if __name__ == '__main__':
    main()
