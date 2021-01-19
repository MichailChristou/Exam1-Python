import json
import urllib.request

data=json.load(open('dictionary.json'))

# loop for every crypto coin in dictionary
for keys in data:
    #construction url to dict
    url="https://min-api.cryptocompare.com/data/pricemulti?fsyms="+keys+"&tsyms=EUR&e=CCCAGG"
    r=urllib.request.urlopen(url)
    html=r.read()
    html=html.decode()
    prices=json.loads(html)
    #isolation of prices and values
    moneydict=(prices[keys])
    eur=(moneydict["EUR"])
    val=(data[keys])
    print("Η αξία του",keys,"είναι: ",int(val)*int(eur))
