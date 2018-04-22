def balsa(M,L,n,T,s):
    for A in range(L):
        for B in range(L):
            M[n][A][B]=0
            if T[n] <=A:
                M[n][A][B]=1
                s[n][A][B]=1
            if T[n]<=B:
                M[n][A][B]=1
                s[n][A][B]=2
    for k in range(n-1,0,-1):
        for A in range(L):
            for B in range(L):
                M[k][A][B]=0
                if T[k]<=A and T[k]>B:
                    M[k][A][B]=M[k+1][A-T[k]][B]+1
                    s[k][A][B]=1
                if T[k]>A and T[k]<=B:
                    M[k][A][B]=M[k+1][A][B-T[k]]+1
                    s[k][A][B]=2
                if T[k]<=A and T[k]<=B:
                    if M[k+1][A-T[k]][B]<M[k+1][A][B-T[k]]:
                        M[k][A][B]=M[k+1][A][B-T[k]]+1
                        s[k][A][B]=2
                    else:
                        M[k][A][B]= M[k+1][A-T[k]][B]+1
                        s[k][A][B] = 1
    return M[0][L][L]


if __name__ == '__main__':
    L= 5
    M = [[[0] * L] * L] * L
