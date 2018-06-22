def f (a , b ):
    a [0][0]=3
    b [1]=2

def g ( c ):
    c [1]=3
    
a =[[0 ,1] ,7]
b=a
c = b [0]
f (a , c )
g(a)
print a ,b , c
