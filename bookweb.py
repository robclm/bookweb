#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
'''
@author: robert
'''

#!/usr/bin/env python
'''
Extra point de projecte web
'''
import urllib2
from bs4 import BeautifulSoup

class Book(object):

    def get_web_page(self, url):
        f = urllib2.urlopen(url)
        html = f.read()
        f.close()

        return html

    def search_text(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        elements = soup.find("div", 'dotd-title')
        print elements.text.strip()


    def main(self):
        html=self.get_web_page("https://www.packtpub.com/packt/offers/free-learning/")
        self.search_text(html)

if __name__ == '__main__':
    web = Book()
    web.main()

