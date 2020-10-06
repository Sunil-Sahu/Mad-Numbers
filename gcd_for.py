a=int(input('Enter you 1st number = '))
b=int(input('Enter you 2nd number = '))
x=[]
y=[]
cf=[]
for i in range(1,a+1):
    if a%i==0:
        x.append(i)
for j in range(1,b+1):
    if b%j==0:
        y.append(j)
for z in x:
    if z in y:
        cf.append(z)

R = cf[-1]
print('the gcd of given numbers is ',R)

