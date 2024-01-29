def my_fun(a,b,c):
    if a>b and a>c:
        lar=a
    elif a<b and b>c:
        lar=b
    else :
        lar=c
    return lar

    
print(my_fun(2,5,6))
