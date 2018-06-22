def concat(a,b):
    new_tupla=()
    for i in a:
        new_tupla=new_tupla+(i,)
    for i in range(len(b)-1,-1,-1):
        new_tupla=new_tupla+(b[i],)
    return new_tupla

def main():
    c=(1,2,3,4)
    d=(5,6,7,9,5,0,1,4)
    e = concat(c,d)
    print e

if __name__ == "__main__":
    main()
