def selchar(a, b):
    s=""
    for i in range(0,len(a),1):
        if i < len(b):
            if len(a[i])>b[i]:
                s=s+a[i][b[i]]
    return s

def main():
    c=('abc','defg','hi','l')
    d=(0,3,1)
    e = selchar(c,d)
    print e

if __name__ == "__main__":
    main()
