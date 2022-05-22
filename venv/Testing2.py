def fibo(n):
    a,b = 1,0

    while a < n:
        print(a , end = " ")
        a,b = a+b ,a

fibo(20)