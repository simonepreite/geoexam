def f (a , b ):
  a [ a [ b ]]= b

def g (a , b ):
  f (a ,1)

def h ( a ):
  g (a , a [3])
  
b =[2 ,10]
a =[ b ,0 ,[1 ,30] ,6]
h(a)
print a , b
