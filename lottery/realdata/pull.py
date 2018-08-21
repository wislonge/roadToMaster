import requests
import re
url="http://datachart.500.com/dlt/?from=17151&to=18097&shujcount=0&sort=0&expect=100"

#querystring = {"expect":"1000"}

headers = {
    'Cache-Control': "no-cache",
    }

response = requests.request("GET", url, headers=headers)
a=response.text

print(a)
b=re.findall(r'<td class="chartBall0+[1-2]">+\d+',a)
print(b)
print(len(b))
#chartBall02
