import json, urllib
dataset = 'S6'
GPSstart = 931035615
GPSend = 933714015
detector = 'H1'

urlformat = 'https://losc.ligo.org/archive/links/{0}/{1}/{2}/{3}/json/'
url = urlformat.format(dataset, detector, GPSstart, GPSend)
print "Tile catalog URL is ", url

r = urllib.urlopen(url).read()
tiles = json.loads(r)

print tiles['dataset']
print tiles['GPSstart']
print tiles['GPSend']

output_list = open('files', 'w')
for file in tiles['strain']:
    if file['format'] == 'hdf5':
        print "found file from ", file['UTCstart']
        print>>output_list, file['url']

output_list.close()
