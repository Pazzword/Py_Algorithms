def merge_sort(arr):
    print(f"Sorting: {arr}")
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        # Recursively sort the two halves
        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        # Merging the sorted halves
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Check if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
        
    print(f"Sorted: {arr}")
    return arr

# Example usage:
example_array = [38, 27, 43, 3, 9, 82, 10]
print("Original array:", example_array)
sorted_array = merge_sort(example_array)
print("Sorted array:", sorted_array)
