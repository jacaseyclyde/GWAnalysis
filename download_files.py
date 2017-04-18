import os, urllib
import numpy
import readligo

try:
    f = open('filesdone')
    donelist = f.readlines()
    f.close()
except:
    donelist = []

urllist = open('files').readlines()
total = len(urllist)

for i, url in enumerate(urllist):
    if url in donelist: continue

    print("Fetching data file ({0}/{1}) from {2}".format(i,total,url))
    r = urllib.urlopen(url.strip()).read()
    f = open('cache/' + url.strip().split('/')[-1], 'w')
    f.write(r)
    f.close()

    f = open('filesdone', 'a')
    print>>f, url
    f.close()
