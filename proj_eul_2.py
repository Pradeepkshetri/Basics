sum=0
i=0
j=1
k=0
while k<=4000000:
    k=i+j
    if k%2==0:
        sum = sum+k
    i=j
    j=k
    
print("The sum of numbers is", sum)

