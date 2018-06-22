s=raw_input("inserire testo: ")

count=1
for i in s:
    if i==" ":
        count=count+1
        
if len(s)==0:
    count=0

print count
