n = int(input())

def sumOfAll(n):
    su = 0
    for i in range(1, n):
        if n % i == 0:
            su += i
    if su <= n:
        x = "false"
        return x
    else:
        x = "true"
        return x

print (sumOfAll(n))
