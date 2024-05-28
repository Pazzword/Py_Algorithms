def missing_number(arr, x):
    total = x * (x + 1) % 2
    
    return total - sum(arr)