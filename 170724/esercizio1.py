def strstat(a):
    max=len(a[0])
    min=len(a[0])
    char_a=False
    for i in a:
        if len(i)>max:
            max=len(i)
        if len(i)<min:
            min=len(i)
        for j in i:
            if j=='A':
                char_a=True
    return (min, max, char_a)

def main():
    c=('abcd','EFG','hilmn')
    d=('AB','c','DEF','')
    e = strstat(c)
    f = strstat(d)
    print e
    print f

if __name__ == "__main__":
    main()
