import random

#εκχώρηση απο τον χρήστη του όρου που θέλει να ελέγξει
print("Δήλωσε τον ν-οστό όρο")
y=int(input())

#αλγόριθμος fibonacci
def fibonacci(x):
    i=1
    j=1
    for k in range (x-2):
        temp=i
        i=i+j
        j=temp
    return i

p=fibonacci(y)
#επανάληψη για τον έλεγχο του  a^p = a mod p
times=0
for g in range (19):
    a=random.randrange(1, p)
    print(a)
    modul= a % p
    ap= (a ** p) % p
    if bool((ap == modul)) == False:
        times=times+1

#έξοδος/εμφάνιση αποτελεσμάτων
if times != 0:
    print("Ο ",y,"- οστός όρος είναι ο",p,"και δεν είναι πρώτος")
else:
    print("Ο ",y,"- οστός όρος είναι ο",p,"και είναι πρώτος")
