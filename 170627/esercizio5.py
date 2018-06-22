def f (a , b ):
    a = a [:]
    a = a + b [1]
    return a
a =[1 ,7]
b =[8 ,[6 ,2]]
c = f (a , b )
print a ,b , c
