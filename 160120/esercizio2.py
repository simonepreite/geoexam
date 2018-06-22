n=raw_input("inserisci intero: ")
n=int(n)
for i in range(-n*n+1, n*n):
    if(i%2!=0):
        print i,
