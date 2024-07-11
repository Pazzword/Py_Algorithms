def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (right + left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return - 1

example_arr = [1,23,13,42,51,26,7,8,19,10,11]

example_target = 42

sorted_arr = sorted(example_arr)

print(sorted_arr)
print(binary_search(sorted_arr, example_target))