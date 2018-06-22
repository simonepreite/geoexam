"""
NOTA: le liste e le tuple sono raffigurate in python come aree di memoria
e ci si accede per riferimento.
Ad esempio la lista a non contiene fisicamente al suo interno copie della
lista b ma riferimenti ad essa.

a ----> [ ° , ° , ° ]
          |   |   |---------->( ° , ° )
          |   |                 |   |
          |   |                 |   |
          |   |                 |   |
          |   |                 |   |
          |   |                 |   |
b---------|---|------>[0,1]<----|---|
"""

def f (a , b ):
  a [ a [ b ][1]]= b

def g ( a ):
  f (a ,1)
  a [0]= a [2]

b =[0 ,1]
a =[ b ,b ,( b , b )]
g(a)
b [1]=2
print a , b
