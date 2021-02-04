import json
import urllib.request

data=json.load(open('dictionary.json'))

#επανάληψη για το κάλεσμα των δεδομένων
for keys in data:
    #δημιουργία του url
    url="https://min-api.cryptocompare.com/data/pricemulti?fsyms="+keys+"&tsyms=EUR&e=CCCAGG"
    r=urllib.request.urlopen(url)
    html=r.read()
    html=html.decode()
    prices=json.loads(html)
    #απομόνωση των prices και values
    moneydict=(prices[keys])
    eur=(moneydict["EUR"])
    val=(data[keys])
    #έξοδος/εμφάνιση αποτελεσμάτων
    print("Η αξία του",keys,"είναι: ",int(val)*int(eur))
