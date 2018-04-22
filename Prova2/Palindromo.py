"""
def palindromo(S,n):
    R=''
    R+=S[::-1]
    M = ['']*len(S)
    print(R)
    for i in range(n):
        for j in range(n):
            if S[i]==R[j]:
                M+=S[i]
    return S
"""
def palindromo2(S,n):
    M = []
    for f in range(n):
        row = [0] * n
        M += [row]
    R = []
    for h in range(n):
        row = [0] * n
        R += [row]
    for i in range(1,n):
        M[i][i]=1
        if i<n:
            M[i][i]=0
    for i in range(n-1,1,-1):
        for j in range(i+1,n):
            if S[i]==S[j]:
                M[i][j]=M[i+1][j-1]+2
                R[i][j]=5
            elif M[i][j-1]>M[i+1][j]:
                M[i][j]=M[i][j-1]
                R[i][j]=1
            else:
                M[i][j]=M[i+1][j]
                R[i][j]=3
    return M[1][n-1],R

def imprimir(S,R,i,j):
    if i==0 or j==0:
        return
    if R[i][j]==5:
        imprimir(S,R,i,j-1)
    elif R[i][j]==1:
        imprimir(S,R,i+1,j)
    elif R[i][j]==3:
        print(S[i]+" "+imprimir(S,R,i+1,j-1)+" "+S[j])

if __name__ == '__main__':
    S='ACGTGTCAAAATCG'
    M,R=palindromo2(S,len(S))
    print(M)
    print(R)