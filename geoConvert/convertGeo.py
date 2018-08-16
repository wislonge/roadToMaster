import requests
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
infile=open("bleStrictGeo.txt")
outfile=open("bleStrictGeoName.txt","w+")
lineArray=infile.readlines()
url = "http://ditu.amap.com/service/regeo"

for linetemp in lineArray:
    idll=linetemp.split('-')    
    print(idll[1])
    print(idll[2])
    querystring = {"longitude":idll[1],"latitude":idll[2]}
    print(querystring)
    headers = {
    'Cache-Control': "no-cache",
    'Postman-Token': "9c871280-32fd-4790-966b-1bc02b39362b"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    objson=json.loads(response.text)
    geostring=objson['data']['desc']
    outfile.write(idll[0]+" "+geostring+"\n")
