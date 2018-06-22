def f (a , b ):
    c=a
    a = a [:]
    b = b [:]
    a [0]= b [0]
    c [0]=5
    return [a ,b , c ]
    
x =[1 ,7]
y =[8 ,[6 ,2]]
z = f (x , y )
print x ,y , z
