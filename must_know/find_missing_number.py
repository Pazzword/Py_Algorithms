# EASY
# Find missing number
def missing_number(arr, x):
    total = x * (x + 1) // 2
    
    return total - sum(arr)


lst = [1,2,3,4,5,6,7,8,10]

target = 10

print(missing_number(lst, 10))      # Output: 9


# MEDIUM
# Find Missing numbers              
from typing import List

class Solution:
    def missing_number(self, arr: List[int], x: int) -> List[int]:
        full_set = set(range(1, x + 1))
        arr_set = set(arr)
        missing = full_set - arr_set
        return sorted(list(missing))

# Create an instance of the Solution class
solution = Solution()

lst = [1, 2, 4, 6, 7, 8, 10]
target = 10

print(solution.missing_number(lst, target))  # Output: [3, 5, 9]

# Test with unsorted list
unsorted_lst = [6, 1, 7, 2, 8, 4, 10]
print(solution.missing_number(unsorted_lst, target))  # Output: [3, 5, 9]
