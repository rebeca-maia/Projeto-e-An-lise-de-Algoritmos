#implementaçao ingênua
def Fib_Rec(n):
    if n==0:
        return 0
    if n==1:
        return 1
    if n>1:
        f=Fib_Rec(n-1)+Fib_Rec(n-2)
        return f

#usando memoização
def Fib_Mem(n):
    memo=[-1]*n
    memo[0]=0
    memo[1]=1
    return Fib_Rec_Rec(n-1,memo)+Fib_Rec_Rec(n-2,memo)

def Fib_Rec_Rec(n,F):
    if F[n]!=1:
        return F[n]
    if n>1:
        F[n]=Fib_Rec_Rec(n-1,F)+Fib_Rec_Rec(n-2,F)
        return F[n]


#usando programação dinâmica
def Fibonacci(n):
    if n<=1:
        return n
    f=[]
    f+=[-1]*n
    f[0]=0
    f[1]=1
    for i in range(2,n):
        f[i]=f[i-1]+f[i-2]
    return f[n-1]

#usando apenas duas variáveis
def Fibonacci2(n):
    if n<=1:
        return n
    a=0
    b=1
    for i in range(2,n):
        b=a+b
        a=b-a
    return b

if __name__ == '__main__':
    a=Fib_Rec(5)
    print(str(a)+"\n")
    b=Fib_Mem(5)
    print(str(b)+"\n")
    c=Fibonacci(5)
    print(str(c)+"\n")
    d=Fibonacci2(5)
    print(d)

