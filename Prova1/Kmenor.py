#questão9
def kmenor(k):
    A = [1, 2, 3, 4, 5, 6, 7, 8]
    B = [9, 10, 11, 12, 13, 14, 15, 16]
    aux = [0, 0, 0, 0, 0, 0, 0, 0]
    if k<0 or k>len(A)+len(B):
        print("error")
    elif k<len(A)+len(B):
        for i in range(0,k):
            j=0
            l=0
            if A[j]<B[l]:
               aux[i]=A[j]
               j+=1
            else:
                aux[i]=B[l]
                l+=1
        return aux[i]
    else:
        if A[len(A)-1]<B[len(B)-1]:
            return A[len(A)-1]
        else:
            return B[len(B)-1]

if __name__=='__main__':
    num=kmenor(3)
    print(num)