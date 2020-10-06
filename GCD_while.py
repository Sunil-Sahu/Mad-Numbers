a=int(input('Enter you 1st number ='))
b=int(input('Enter you 2nd number ='))
i=1
j=1
x=[]
y=[]
while i<=a:
    if a%i==0 :
        x.append(i)
        i+=1
    else :
        i+=1
print('factors of ',a,'are ',x,'\n')
while j<=b:
    if b%j==0 :
        y.append(j)
        j+=1
    else :
        j+=1
cf= []
for f in x:
    if f in y:
        cf.append(f)

p=(cf[-1])
print('factors of ',b,'are ',y,'\n')
print('The GCD of given values is',p)
