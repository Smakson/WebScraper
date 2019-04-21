# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 17:28:56 2017

@author: Miha
"""
import os.path
from bs4 import BeautifulSoup
from urllib.request import urlopen
import io


#the default URL for the whole website of interest
s = 'http://giskd2s.situla.org/rkd/Opis.asp?Esd='


def open_soup(i):
    """Takes in an integer i as input and returns a BeautifulSoup object
    with the URL of the relevant s + i."""
    with urlopen(s + str(i)) as url:
        soup = BeautifulSoup(url.read(), 'lxml')
    return soup



def data_obtainer(soup):
    """Takes in a BeautifulSoup object as an argument, searches
    it for all the necessary font strings, and returns the resulting list."""
    temp = soup.body.table(string = data_certifier)
    return temp[2: (len(temp) - 1)]

def data_nicefier(string):
    """Takes in a 'string' and makes it nicer by stripping away all the unecessary parts
    and properly formatting it."""
    return ' '.join(string.split())

def improved_search(strings, searched, start):
    """Takes in three arguments: a list of 'strings', a string 'searched', and
    an integer start. The functions compares each element of the list to the
    string 'searched' and returns the index at which it finds the match."""
    for i in range(start, len(strings)):
        if strings[i] == searched:
            return i
#lokacija start = 25,  x = 'Lokacija:'
#občina start = 23, x = Občina:
#ime enote index = 4,  x = 'Ime enote: \r\n                  '
#tekst opis index = 15 , x = 'Tekstualni \r\n                  opis enote:'
#datacija index = 17  , x = 'Datacija enote:'



            
def selector(strings, lokacija_ind):
    """Takes in a list of strings and determines whether they are useful or not."""
    return not ((len(strings) < 5) or (strings[lokacija_ind + 1] == 'PRISTOJNOSTI'))



"""def data_writer(strings, lokacija_ind):
    obcina_ind = improved_search(strings, 'Občina:', 23)
    obcina = data_nicefier(strings[obcina_ind + 1]).upper()
    path = 'TEKSTI/' + obcina + '.txt'
    string = '\n' + data_stringyfier(strings, lokacija_ind)
    if os.path.exists(path):
        with io.open(path, 'a', encoding="utf-8") as file:
            file.write(string)
    else:
        with io.open(path, 'w', encoding="utf-8") as file:
            helper = "OBČINA {0}- OBČINA {0}- OBČINA {0}- OBČINA {0}\nREGISTER NEPREMIČNINE KULTURNE DEDIŠČINE \nREPUBLIKA SLOVENIJA \nMINISTRSTVO ZA KULTURO\nPOGOJI UPORABE\nPri uporabi podatkov iz registra mora vsak uporabnik register navesti kot vir podatkov (Zakon o varstvu kulturne dediščine, Uradni list RS, št. 16/2008).\nSEZNAM NEPREMIČNE KULTURNE DEDIŠČINE – OBČINA {0}\n\n".format((obcina))
            print(helper)
            string =  helper + string
            file.write(string)    
"""


        
    
def data_certifier(string):
    """Acts as a filter functions on a string and returns true if
    the string is not '\n' or '\xa0 and else otherwise."""
    return not ((string == '\n') or (string[ : 1] == '\xa0' ) or (string == ' '))



