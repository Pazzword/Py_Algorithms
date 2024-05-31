# F(n) = F(n-1) + F(n-2)


# EASY (and slow)
def is_fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return is_fibonacci(n-1) + is_fibonacci(n-2)
    
#print(is_fibonacci(40))

# MEDIUM
# Efficient way
def is_fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        memo[n] = is_fibonacci(n-1, memo) + is_fibonacci(n-2, memo)
        return memo[n]

print(is_fibonacci(40))  # This will run much faster