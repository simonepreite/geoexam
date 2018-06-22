def f (a , b ):
  a [ b ]= a [ b ]+ a [ b ]

def g ( a ):
  f (a ,0)
  a [1]=5
  
a =[(4 ,7) ,[7 ,4]]
b = a [0]
c = a [1]
g(a)
print a ,b , c
