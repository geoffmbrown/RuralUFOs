# -*- coding: utf-8 -*-
"""
NUFORCscrape.py
@author: Geoff Brown, Northeastern Illinois University
email: g-brown9@neiu.edu

license: CC BY-NC-SA 2.0 (feel free to share and adapt, but non-commercially
and you must give attribution)

This script was created to webscrape UFO sighting data from NUFORC.org
Data was collected for this project using this code on August 31, 2018.

NUFORC data is posted on the web in batches of 1000.
There were 142 batches uploaded when this script was run.

This script iterates over every number in a batch and fetches the text stored at
a specific point on the corresponding page. The text is then stored as a list.

The list (each sighting) is written as a row to a .csv file. Every value in the
lists (every piece of text surrounding <br> tags) is written as a new columnself.

The result is a file titled NUFORCraw.csv
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
