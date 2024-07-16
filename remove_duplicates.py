from typing import List

# EASY
def remove_duplicates(arr):
    return list(set(arr))

example = ["sprinkle", "anzor", "nina", "nina", "anzor"]

print(remove_duplicates(example))



# MEDIUM EASY
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[::] = sorted(set(nums))
        return len(nums)