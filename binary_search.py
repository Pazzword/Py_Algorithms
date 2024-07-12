from typing import List

class Solution:
    def binary_search(self, arr: List[int], x: int) -> int:
        left, right = 0, len(arr) + 1
        while left <= right:
            mid = (left + right)  // 2
            if arr[mid] == x:
                return mid
            elif arr[mid] < x:
                left = mid + 1
            else:
                right = mid - 1
        return - 1

example_arr = [1,23,13,42,51,26,7,8,19,10,11]

example_target = 42

sorted_arr = sorted(example_arr)

print(sorted_arr)
print(Solution().binary_search(sorted_arr, example_target))