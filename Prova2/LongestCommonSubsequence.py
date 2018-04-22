def scl(X,Y,m,n):
    T = []
    S=[]
    for f in range(m):
        row = [0] * n
        T += [row]

    for l in range(m):
        row = [''] * n
        S += [row]
    for y in range(m):
        T[y][0]=0
    for j in range(n):
        T[0][j]=0
    u=0
    for i in range(1,m):
        for j in range(1,n):
            if X[i]==Y[j]:
                T[i][j]=T[i-1][j-1]+1
                S[i][j]="diagonal"
                u+=1
            else:
                if T[i-1][j]>T[i][j-1]:
                    T[i][j]=T[i][j-1]
                    S[i][j]="left"
                    u += 1
                else:
                    T[i][j]=T[i-1][j]
                    S[i][j]="top"
                    u += 1
    print(u)
    return T[m-1][n-1]

def write(S,X,i,j):
    if i!=0 and j!=0:
        if S[i][j]=="left":
            write(S,X,i,j-1)
        elif S[i][j] =="top":
            write(S,X,i-1,j)
        elif S[i][j]=="diagonal":
            write(S,X,i-1,j-1)
            print(X[i])



if __name__ == '__main__':
    X=['B','D','C','A','B','A']
    Y=['A','B','C','B','D','A','B']
    m=len(X)
    n=len(Y)
    fin=scl(X,Y,m,n)
