"""
questo programma sostituisce gli spazi con un ,spazio
utilizziamo lo slicing per comporre la stringa
"""

s=raw_input("inserire testo: ")
i = 0
lung = len(s)
while i < lung:
    if s[i]==' ':
        s=s[:i]+','+s[i:]
        lung=lung+1
        i=i+1
    i=i+1
print s
