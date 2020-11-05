count=0
x=1
n=5


def prime(x):
    c=0
    for i in range (1,x+1):
        if x%i==0:
            c=c+1
    if c==2:
        return 1
    else:
        return 0


while count<=n:
    count=count+prime(x)
    if count==n:
        break
    x=x+1

print(count)
print("The",n,"th prime number is", x)




    





     