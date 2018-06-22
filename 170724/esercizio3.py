def media(a,b):
    return (55,62,79,92,94,97,67,90,78,118,110,90)

city=raw_input("insert city: ")
year=int(raw_input("insert year: "))

piov_med=media(city, year)
cont=0
for i in piov_med:
    if i>100:
        cont=cont+1
print cont
