import os, urllib
import numpy
import readligo

try:
    f = open('L1filesdone')
    donelist = f.readlines()
    f.close()
except:
    donelist = []

urllist = open('L1files').readlines()
total = len(urllist)

for i, url in enumerate(urllist):
    if url in donelist: continue

    print("Fetching data file ({0}/{1}) from {2}".format(i,total,url))
    r = urllib.urlopen(url.strip()).read()
    f = open('cache/L1/' + url.strip().split('/')[-1], 'w')
    f.write(r)
    f.close()

    f = open('L1filesdone', 'a')
    print>>f, url
    f.close()
