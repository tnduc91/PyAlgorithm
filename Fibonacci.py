'REF: https://www.youtube.com/watch?v=vYquumk4nWw'

def fib_bottom_up(n):
    if n == 1 or n == 2:
        return 1

    bottom_up = [None] * (n+1)
    bottom_up[1] = 1
    bottom_up[2] = 1
    for i in range(3, n+1):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]

    return bottom_up[n]

def fib_recursive(n):
    if n == 1 or n == 2:
        return 1;
    return  fib_recursive(n-1) + fib_recursive(n-2)

def fib_2(n, meno):
    if meno[n] is not None:
        return meno[n];
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib_2(n-1, meno) + fib_2(n-2, meno)

    meno[n] = result
    return result;

def fib_memo(n):
    memo = [None] * (n+1)
    return fib_2(n, memo)

print(fib_bottom_up(35))
print(fib_recursive(35))
print(fib_memo(35))