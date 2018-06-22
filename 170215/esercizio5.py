def f ( a ):
  c = a [0]
  a [0]= a [1]
  a [1]= c
  return a

def h (b , a ):
  return a [ b [0]]
  
a =[0 ,7]
b =[ f ( a ) , f ( a )]
c = h (a , b )
print a ,b , c
