def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1)**2 + recur_fibo(n-2))

def Fibonacci(n):
    if n<= 0:
        print("Incorrect input")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return Fibonacci(n-1)**2 + Fibonacci(n-2)

# input N
nterms = int(input("Input n : "))
if nterms <= 0:
   print("Plese enter a positive integer")
else:
    print("sequence : ")
    for i in range(nterms):
       print(recur_fibo(i),end=' ')
    print('\n')
    print("n-th : ")
    print(Fibonacci(nterms))
 
