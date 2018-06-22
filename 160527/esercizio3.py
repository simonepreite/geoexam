n=int(raw_input("iserisci primo intero: "))
m=int(raw_input("inserisci secondo intero: "))

max=0
min=0

if n>m:
    max=n
    min=m
else:
    max=m
    min=n
for i in range(min*min, max*max+1,1):
    print i,
