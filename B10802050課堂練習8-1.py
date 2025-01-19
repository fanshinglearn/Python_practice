def factorial(n):
    fac = 1
    for i in range(1, n+1):
        fac *= i
    return fac

n = int(input('請輸入欲計算的階乘 : '))
print('%d! = %d'%(n, factorial(n)))
