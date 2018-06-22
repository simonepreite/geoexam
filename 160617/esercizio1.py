"""
le due funzioni lon e lat sono finte, servono solo a testare il
programma principale
"""

def lat(city):
    return 'N41.91'

def lon(city):
    return 'E12.46'

def latlon(a):
    tupl=()
    for i in a:
        emis=True
        if lat(i)[0]!='N': #sto dicendo che se la citta' si trova nell'emisfero sud imposto a false l'ultimo parametro della tupla
            emis=False
        temp=(lat(i), lon(i), emis);
        tupl=tupl+(temp,)
    return tupl

def main():
    c=('Roma','Milano','Napoli')
    e = latlon(c)
    print e

if __name__ == "__main__":
    main()
