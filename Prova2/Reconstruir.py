def dic(frase):
    if frase =='eu' or frase =='amo' or frase =='programação' or frase =='dinâmica':
        return True
    else:
        return False

def reconstruct(S,n):
    B=[]
    for i in range(n+1):
        for j in range(n,-1,-1):
            if dic(S[i:j]):
                B.append(S[i:j]+" ")

    print("".join(B))

if __name__ == '__main__':
    S="euamoprogramaçãodinâmica"
    reconstruct(S,len(S))

