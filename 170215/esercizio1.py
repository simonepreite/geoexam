def swap(a):
    tup=()
    for i in range(1,len(a),2):
        tup=tup+(a[i],a[i-1])
    if len(a)%2:
        tup=tup+(a[-1],)
    return tup

def main():
    c=(7,8,1,3)
    d=(2,5,3)
    e = swap(c)
    f = swap(d)
    print e
    print f

if __name__ == "__main__":
    main()
