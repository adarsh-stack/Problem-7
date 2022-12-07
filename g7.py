# Question 7

l=int(input("enter the limit: "))
for i in range(0,l):
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c+=1
    if c==2:
        print(i)