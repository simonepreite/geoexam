n=int(raw_input("inserisci primo intero: "))
m=int(raw_input("inserisci secondo intero: "))
#cast del numero da stringa a intero inline direttamente sulla chiamata della funzione raw_input
if n < m:
    for i in range(n, m+1, 1):
        if i%n==0:
            print i,
else:
    print "error, primo numero piu' grande del secondo"
