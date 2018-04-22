#questão7
def dec(S,R,p,r,piv):
    a,b,c=0
    for k in range(p,r):
        if S[k]<piv:
            a+=1
        elif S[k]==piv:
            b+=1
        else:
            c+=1
    b+=a
    c+=b
    for k in range(p,r):
        if S[k]<piv:
            R[p+a-1]=S[k]
            a-=1
        elif S[k]==piv:
            R[p+b-1]=S[k]
            b-=1
        else:
            R[p+c-1]=S[k]
            c-=1
    return p+b-1,p+c-1


