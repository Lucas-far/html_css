

"""

"""

from random import choice

def character_sequence_maker():
    alfabeto = [*'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'.split(',')]
    inteiros = [*'1,2,3,4,5,6,7,8,9'.split(',')]
    resultado = []
    index = 0
    while index < 5:
        resultado.extend(choice(alfabeto))
        resultado.extend(choice(inteiros))
        index += 1
    for string in resultado:
        print(string, end='')
