def mult(a, b):
    tupl=()
    if len(a)==len(b):
        for i in range(0, len(a), 1):
            temp=0
            if a[i]:
                temp=b[i]*2
            else:
                temp=b[i]*-2
            tupl=tupl+(temp,)
    return tupl

def main():
    c=(True, False, True)
    d=(2,3,-4)
    e = mult(c,d)
    print e

if __name__ == "__main__":
    main()
