
def merge_prof(a , b ):
    c =[]
    for i in range (0 , min ( len ( a ) , len ( b ))):
        c = c +[( a [ i ] , b [ i ])]
    for i in range ( len ( a ) , len ( b )):
        c = c +[ b [ i ]]
    for i in range ( len ( b ) , len ( a )):
        c = c +[ a [ i ]]
    return c

def merge(a,b):
    dim_list=0
    i=0
    new_list=[]
    if len(a) <= len(b):
        dim_list=len(a)
    else:
        dim_list=len(b)
    while i < dim_list:
        new_list=new_list+[(a[i],b[i])]
        i=i+1
    if len(a) > len(b):
        while i < len(a):
            new_list=new_list+[a[i]]
            i=i+1
    elif len(b) > len (a):
        while i < len(b):
            new_list=new_list+[b[i]]
            i=i+1
    return new_list


def main():
    c=[1,2,3,4]
    d=[5,6,7,9,5,0,1,4]
    e = merge(c,d)
    f = merge_prof(c,d)
    print (e)
    print (f)

if __name__ == "__main__":
    main()
