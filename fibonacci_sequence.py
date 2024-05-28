# F(n) = F(n-1) + F(n-2)

def is_fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return is_fibonacci(n-1) + is_fibonacci(n-2)
    
print(is_fibonacci(6))