s=raw_input("inserisci espressione: ")

for i in range(0,len(s),1):
    if s[i]=="+":
        first=s[:i]
        second=s[i+1:]
        try:
            int(first)
            int(second)
        except:
            print "Not integer number!"
            exit()
        print first
        print second
