# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 17:28:15 2017

@author: Miha
"""



#libraries
from bs4 import BeautifulSoup
from urllib.request import urlopen
from filter1 import open_soup
from filter1 import data_obtainer
from filter1 import improved_search
#from filter1 import selector
#from word import doc_writer
from word import file_writer
import time
import urllib

#the default URL for the whole website of interest
s = 'http://giskd2s.situla.org/rkd/Opis.asp?Esd='

def one(i):
    """One repetition of main, for testing purposes"""
    soup = open_soup(i)
    data =  data_obtainer(soup)
    lokacija = improved_search(data, 'Lokacija:', 25)
    if len(data) > 5:
        file_writer(data, lokacija)




def main(start, end):
    """The functions loops through all the URLs of
    the above family and from an ešd number of start to end. It reads the HTML content of each URL and passes
    it down to functions from 'filter1.py' which obtain the necessary data from it and write it down to the corresponding folder"""
    for i in range(start, end):
        print(i)
        global x
        x = i
        completed = False
        while not completed:
            try:    
                one(i)
                completed = True
            except Exception:
                pass
            time.sleep(1)
            
            
        

