def missing(arr, x):
    full_set = set(range(1, x + 1))
    arr_set = set(arr)
    missed = full_set - arr_set
    return(sorted(list(missed)))