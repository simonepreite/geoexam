def repl(a,b):
    new_tupla=()
    if len(a)==len(b):
        for i in range(0,len(a),1):
            j=0
            while j<a[i]:
                new_tupla=new_tupla+(b[i],)
                j=j+1
    return new_tupla
    
def main():
    c=(1,2,3,4)
    d=(5,6,7,9)
    e = repl(c,d)
    print e

if __name__ == "__main__":
    main()
