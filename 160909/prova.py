def f ( a ):
    a [0][0]= a [0][0]+1
    a [1][0]= a [1][0] -1
    return a [1]

def g ( c ):
    c [1]=4
    return c [0]
    
a =[[0 ,1] ,[2 ,3]]
a [1][1]= g ( f ( a ))
print a
