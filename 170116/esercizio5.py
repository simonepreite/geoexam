def f (a , b ):
  c=a[b]
  a [ b ]= a [ b ]+1
  return c

def g ( b ):
  return b [2]
  
a =[0 ,1 ,2]
b =[1 ,2 , a [1] , a [2]]
a [0]= f (a ,1)
print a , g ( b )
