def sequenciacontigua(S,n):
    C=[0]*n
    R=[0]*n
    C[0]=S[0]
    R[0]=1
    max=1
    for i in range(1,n):
        if S[i]<S[i]+C[i-1]:
            C[i]=S[i]+C[i-1]
            R[i]=R[i-1]
        else:
            C[i]=S[i]
            R[i]=i
        if C[i]>C[max]:
            max=i
    write(S,R,max)

def write(S,R,max):
    for i in range(R[max],max+1):
        print(S[i])

if __name__ == '__main__':
    S = [5,15,-30,10,-5,40,10]
    sequenciacontigua(S,len(S))