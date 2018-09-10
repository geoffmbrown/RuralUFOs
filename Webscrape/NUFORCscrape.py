# -*- coding: utf-8 -*-
"""
NUFORCscrape.py
@author: Geoff Brown, g-brown9@neiu.edu

This script was created to webscrape UFO sighting data from NUFORC.org

NUFORC data is posted on the web in batches of 1000.
Data was collected for this project using this code on August 30, 2018.
"""

from lxml import html
import requests, csv
import lxml
import re

batch = 1

while batch <=142:
    for scount in range (1,1001):
        try:
            sstr = str(scount)
            snum = sstr.zfill(3)
            bstr = str(batch)
            bnum3 = bstr.zfill(3)
            bnum2 = bstr.zfill(2)
            site = ('http://www.nuforc.org/webreports/' + bnum3 + '/S' + bnum2 + snum + '.html')
            sightget = requests.get(site)
            sightdata = html.fromstring(sightget.content)
            sightpath = sightdata.xpath('//tbody/tr/td/font/text()')
            sighting = [sightpath]
            error = ['error on:', site]
            with open("NUFORCraw.csv", "a") as fp:
                wr = csv.writer(fp, dialect='excel')
                slist = [bstr, site]
                for each_sight in sighting:
                    srep = [w.replace("/n", "") for w in each_sight]
                    slist.extend(srep)
                    wr.writerow(slist)
        except lxml.etree.XMLSyntaxError:
            print('error on ' + site)
            with open("NUFORCraw.csv", "a") as fp:
               wr = csv.writer(fp, dialect='excel')
               wr.writerow(error)
            continue
        except UnicodeEncodeError:
            print('Unicode error on ' + site)
            with open("NUFORCraw.csv", "a") as fp:
               wr = csv.writer(fp, dialect='excel')
               wr.writerow(error)
    if scount == 1000:
        batch = batch + 1
        print('batch # ' + bstr + ' done...')
