import urllib.request
import json
from datetime import date , timedelta

today = date.today()
day = today.strftime("%d")

d = int(day)                #μετατροπή της μεταβλητής day σε int

arr=[]                      #λιστα για τους νικητηριους αριθμους
sumdata = [0] * 80          #λιστα για το ποσες φορες βρισκω εναν αριθμο
totaldata = [0] * 80

#επανάληψη για το κάλεσμα των δεδομένων
for x in range(d):
        thisday = today + timedelta(days=-x)
        thisday = str(thisday)
        # δημιουργία του url
        url = "https://api.opap.gr/draws/v3.0/1100/draw-date/"+thisday+"/"+thisday
        r = urllib.request.urlopen(url)
        html = r.read()
        html = html.decode()
        data = json.loads(html,strict=False)
        for draw in data["content"]:
            arr.append(draw["winningNumbers"]["list"])      #αποθήκευση των νικητήριων αριθμών
            i=1
            if i==1:
                break

#επανάληψη για τον υπολογισμό του πλήθους εμφανίσεων των αριθμών
for i in range(d):
    for j in range(20):
        sumdata[(arr[i][j]-1)]=sumdata[(arr[i][j]-1)]+1

#επανάληψη για τον υπολογισμό του ποσοστού
for i in range(80):
    totaldata[i]=sumdata[i]/(20*d)*100

#επανάληψη για την έξοδο/εμφάνιση αποτελεσμάτων
for i in range(80):
    print("Ο αριθμος ",i+1," εμφανιστηκε ",sumdata[i]," φορες στις πρωτες κληρωσεις των ημερων τον τελευταιο μηνα και αποτελουσε το ", totaldata[i],"% των αριθμων που κληρωθηκαν")
