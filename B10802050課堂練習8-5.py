n = int(input('n: '))

def odd(n):
    if n == 1:
        return 1
    else:
        if n % 2 != 0:
            return (n + odd(n-1))
        else:
            return odd(n - 1)

print(odd(n))