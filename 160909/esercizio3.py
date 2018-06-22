s=raw_input("inserire testo: ")

min_voc=['a','e','i','o','u']
lock_voc=['A','E','I','O','U']

for i in range(0,len(s),1):
    for j in range(0, len(min_voc),1):
        if s[i]==min_voc[j]:
            s=s[:i]+lock_voc[j]+s[i+1:]
print s
