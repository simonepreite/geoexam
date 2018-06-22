s=raw_input("inserisci testo: ")
i=0
lung = len(s)
while i<lung:
    if s[i]==" ":
        s=s[:i]+s[i+1:]
        lung=lung-1
        i=i-1
    i=i+1

d=""
for i in range(1, len(s),2):
    d=d+s[i]

"""
per posizione pari inizia a contare da 1 anzichè da 0 
quindi il primo carttere che si trova in posizione 0 va
omesso, facciamo partire così la funzione range da 1
"""

print s
print d
