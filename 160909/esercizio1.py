def eventuple(a, b):
    tupl=()
    min=a
    max=b
    if b<a:
        min=b
        max=a
    for i in range(min,max+1,1):
        if i%2==0:
            tupl=tupl+(i,)
    return tupl

def main():
    e = eventuple(-2,5)
    print e

if __name__ == "__main__":
    main()
