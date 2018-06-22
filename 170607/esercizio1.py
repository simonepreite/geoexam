def count(a):
    c_true=0
    c_false=0
    for i in a:
        if i:
            c_true=c_true+1
        else:
            c_false=c_false+1
    return (c_true, c_false)

def main():
    c=(True, False, True, True, False)
    e = count(c)
    print e

if __name__ == "__main__":
    main()
