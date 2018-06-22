s=raw_input("inserisci stringa: ")
t=raw_input("inserisci carattere: ")

if len(t)==1:
    for i in range(0, len(s), 1):
        print s[i]
        if s[i]==t:
            print i,
else:
    print "hai inserito piu' di un carattere nella seconda stringa"
