num=7
fact=1
if num<0:
    print("it can't be negitive")
elif num==0:
    print("can't be 0")    
else:
    for i in range(1,num+1):
        fact=fact*i
    print(fact)    
