def ultimieventi(a,b):
    return ((3.2,'15.02.2016'),(3.5,'20.11.2016'),(2.9,'11.02.2017'))


city=raw_input("insert city: ")
eventi=ultimieventi(2,city)
count=0
for i in eventi:
    if i[0]>3:
        count=count+1
print count
