def fibo(n):
	#print(n)
	i = 1
	f1 = 1
	f2 = 0
	temp = 0
	while i < n:
		#print(f1, " + ",f2, " =", f1 + f2)
		temp = f1
		f1 = f1 + f2
		f2 = temp
		i = i + 1
	print("el factorial",n,"-esimo es: ", f1 + f2)

def fibo_recur(n, indice, fib1, fib2):
	if indice < n:
		#print(fib1, " + ",fib2, " =", fib1  + fib2 )
		temp = fib1 
		fib1  = fib1  + fib2 
		fib2  = temp
		indice  = indice  + 1
		fibo_recur(n, indice, fib1, fib2)
	else:
		print("Fin de la función recursiva")
		print("el factorial",n,"-esimo es: ", fib1  + fib2 )
        

print(fibo(10))
indice = 1
fib1 = 1
fib2 = 0
print(fibo_recur(10, indice, fib1, fib2))