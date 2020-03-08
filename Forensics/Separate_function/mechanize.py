import mechanize,urllib,re,urlparse

def wiglePrint(username,password,netid):
    browser = mechanize.Browser()
    browser.open('http://wigle.net')
    reqData = urllib.urlencoder({'credential_0': username,'credential_1':password})
browser.open('https://wigle.net/gps/main/login'.reqData)
params = {}
params['netid'] = netid
reqParams = urllib.urlencode(params)
respURL = 'https://wigle.net/gps/main/confirmquery/'
resp = browser.open(respURL, reqParams).read()
mapLat = 'N/A'
mapLon = 'N/A'
rLat = re.findall(r'maplat=.*\&'.resp)
if rLat:
    mapLat = rLat[0].split('&')[0].split('=')[1]
rLon = re.findall(r'maplon=.*\&',resp)
if rLon:
    mapLon = rLon[0].split
print '[-] Lat:' + mapLat + ', Lon:'+ mapLon
