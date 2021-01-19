import urllib.request
import json
from datetime import date

today = date.today()
year = today.strftime("%y")
month = today.strftime("%m")
day = today.strftime("%d")

d = int(day)
m = int(month)
y = int(year)

arr=[]                      #λιστα για τους νικητηριους αριθμους
sumdata = [0] * 80          #λιστα για το ποσες φορες βρισκω εναν αριθμο
totaldata = [0] * 80

for x in range(1,d+1):

        url = "https://api.opap.gr/draws/v3.0/1100/draw-date/2021-01-01/2021-01-01"
        r = urllib.request.urlopen(url)
        html = r.read()
        html = html.decode()
        data = json.loads(html,strict=False)
        for draw in data["content"]:
            arr.append(draw["winningNumbers"]["list"])      #αποθηκευση των νικητηριων αριθμων
            i=1
            if i==1:
                break
        day = str(d-x)

for i in range(d):
    for j in range(20):
        sumdata[(arr[i][j]-1)]=sumdata[(arr[i][j]-1)]+1

for i in range(80):
    totaldata[i]=sumdata[i]/(80*d)*100 #na dioruvsv to lauow me ta pososta

for i in range(80):
    print("Ο αριθμος ",i+1," εμφανιστηκε ",sumdata[i]," φορες στις πρωτες κληρωσεις των ημερων τον τελευταιο μηνα και αποτελουσε το ", totaldata[i],"% των αριθμων που κληρωθηκαν")