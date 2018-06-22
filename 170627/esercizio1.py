def lencheck(a):
    count=0
    disp=False
    for i in a:
        count=count+len(i)
        if len(i)%2:
            disp=True
    return (count, disp)

def main():
    c=('abc','efg','hijl')
    d=('ab','cd','efgh','')
    e = lencheck(c)
    f = lencheck(d)
    print e
    print f

if __name__ == "__main__":
    main()
