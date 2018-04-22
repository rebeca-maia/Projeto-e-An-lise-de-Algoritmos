import random
f = []
s = []
a=[]
t=[]

f_ = 0
s_ = 0

n=100
fim=0

for r in range(2):
    row = [0] * n
    f += [row]

for y in range(2):
    row = [0] * n
    t += [row]

for q in range(2):
    row = [0] * n
    a += [row]

for v in range(2):
    row = [0] * n
    s += [row]

x1= random.randint(1,10)%10
x2= random.randint(1,10)%10
e1=random.randint(1,10)%10
e2=random.randint(1,10)%10

for i in range(100):
    t[0][i]=random.randint(1,10)%10
    t[1][i] = random.randint(1,10)%10
    a[0][i]=random.randint(1,10)%10
    a[1][i]=random.randint(1,10)%10



f[0][0]=e1+a[0][0]
f[1][0]=e2+a[1][0]

for k in range(1,n):
    if f[0][k-1]<f[1][k-1]+t[1][k-1]:
        f[0][k]=f[0][k-1]+a[0][k]
        s[0][k]=1
    else:
        f[0][k]=f[1][k-1]+t[1][k-1]+a[0][k]
        s[0][k]=2
    if f[1][k-1]<f[0][k-1]+t[0][k-1]:
        f[1][k]=f[1][k-1]+a[1][k]
        s[1][k]=2
    else:
        f[1][k]=f[0][k-1]
if f[0][n-1]+x1 < f[1][n-1]+x1:
    f_+=f[0][n-1]+x1
    s_+=1
else:
    f_+=f[1][n-1]+x2
    s_+=2

if f[0][99]+x1<f[1][99]+x2:
    fim = f[0][99]+x1
else:
    fim = f[1][99]+x2

