"""
import math

def mediana(X,Y,a,a1,b,b1):
    m1=math.floor((a+a1)/2)
    m2=math.floor((b+b1)/2)
    if a==a1:
        return X[a]
    if X[m1]==Y[m2]:
        return X[m1]
    if X[m1]>Y[m2]:
        return mediana(a,m1,m2,b)
    else:
        return mediana(m1,a1,b,m2)
"""
#questão8
def mediana(X,Y,aux):
    #m = 0
    tam1 = len(X)
    tam2 = len(Y)
    tam_fin = ((tam1 + tam2) // 2)
    i = 0
    j = 0
    for k in range(0, tam_fin + 1):
        if i < len(X) and X[i] <= Y[j]:
            aux[k] = X[i]
            i =1+i
        else:
            aux[k] = Y[j]
            j=1+j

    if ((tam1 + tam2) % 2 == 0):
        m = (aux[tam_fin] + aux[tam_fin - 1]) // 2
    else:
        m = aux[tam_fin - 1]
    print(m)



if __name__ == '__main__':
    X=[1,2,3,4,5,6]
    Y=[10,20,30,40,50,60]
    aux=[0,0,0,0,0,0]
    mediana(X,Y,aux)