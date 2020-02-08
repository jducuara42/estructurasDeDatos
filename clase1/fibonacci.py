def fibo(n):
    #print(n)
    i = 1
    f1 = 1
    f2 = 0
    temp = 0
    while i < n:
        print(f1, " + ",f2, " =", f1 + f2)
        temp = f1
        f1 = f1 + f2
        f2 = temp
        i = i + 1
        
        
print(fibo(10))
